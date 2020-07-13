# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Functions related to climate indices.
#
# Authors:
# 1. rousseau.yannick@ouranos.ca
# (C) 2020 Ouranos, Canada
# ----------------------------------------------------------------------------------------------------------------------

import config as cfg
import glob
import math
import numpy as np
import os.path
import pandas as pd
import plot
import utils
import warnings
import xarray as xr
import xclim.indices as indices
import xclim.subset as subset
from scipy.interpolate import griddata


def calc_idx_ts(idx_name, idx_threshs):

    """
    --------------------------------------------------------------------------------------------------------------------
    Calculate an index.
    TODO: Determine if the curve needs to correspond to the mean or median value. It is currently the mean value, but it
          would make more sense to use median in this type of analysis.
          Determine if the curve needs to come from observations or from climate scenarios. It is currently associated
          with observations, and I think this is the way to do it. However, the lower and upper limits (the grey zone)
          are associated with climate scenarios.

    Parameters:
    idx_names : str
        Index name.
    idx_threshs : [float]
        Threshold values associated with each indicator.
    --------------------------------------------------------------------------------------------------------------------
    """

    # Reference period.
    years_ref   = [cfg.per_ref[0], cfg.per_ref[1]]
    dates_ref   = [str(years_ref[0]) + "-01-01", str(years_ref[1]) + "-12-31"]

    # Future period.
    years_fut   = [cfg.per_ref[1], cfg.per_fut[1]]
    dates_fut   = [str(years_fut[0]) + "-01-01", str(years_fut[1]) + "-12-31"]
    n_years_fut = cfg.per_fut[1] - cfg.per_ref[1] + 1

    # Emission scenarios.
    rcps = ["ref"]
    for rcp in cfg.rcps:
        rcps.append(rcp)

    # Select variables.
    vars = []
    if idx_name == cfg.idx_tx_days_above:
        vars = [cfg.var_cordex_tasmax]

    # Loop through stations.
    for stn in cfg.stns:

        # Verify if this variable is available for the current station.
        vars_avail = True
        for var in vars:
            if not(os.path.isdir(cfg.get_d_sim(stn, cfg.cat_qqmap, var))):
                vars_avail = False
                break
        if not(vars_avail):
            continue

        # Loop through emissions scenarios.
        ds_rcp_26 = None
        ds_rcp_45 = None
        ds_rcp_85 = None
        for rcp in rcps:

            utils.log("-", True)
            utils.log("Index             : " + idx_name, True)
            utils.log("Station           : " + stn, True)
            utils.log("Emission scenario : " + cfg.get_rcp_desc(rcp), True)
            utils.log("-", True)

            # Analysis of simulation files -----------------------------------------------------------------------------

            utils.log("Collecting simulation files.", True)

            # List simulation files. As soon as there is no file for one variable, the analysis for the current RCP
            # needs to abort.
            n_sim = 0
            p_sim = []
            for var in vars:
                if rcp == "ref":
                    p_sim_i = cfg.get_d_sim(stn, cfg.cat_obs, "") + var + "/" + var + "_" + stn + ".nc"
                    if os.path.exists(p_sim_i) and (type(p_sim_i) is str):
                        p_sim_i = [p_sim_i]
                else:
                    p_format = cfg.get_d_sim(stn, cfg.cat_qqmap, "") + var + "/*_" + rcp + ".nc"
                    p_sim_i = glob.glob(p_format)
                if not(p_sim_i):
                    p_sim = []
                else:
                    p_sim.append(p_sim_i)
                    n_sim = len(p_sim_i)
            if not p_sim:
                continue

            utils.log("Calculating climate indices", True)

            # Loop through simulations.
            ds_idx_ref_mean = None
            ds_idx_ref_min = None
            ds_idx_ref_max = None
            ds_idx_fut_mean = None
            ds_idx_fut_min = None
            ds_idx_fut_max = None
            ds_idx_ref = None
            ds_idx_fut = None
            for sim in range(0, n_sim):

                # Scenarios --------------------------------------------------------------------------------------------

                # Load datasets (one per variable).
                ds_scen = []

                for var in range(0, len(vars)):
                    ds = xr.open_dataset(p_sim[var][sim])
                    ds_scen.append(ds)

                # Adjust units.
                idx_threshs_str = []
                for i in range(0, len(ds_scen)):
                    if rcp == "ref":
                        for idx_thresh in idx_threshs:
                            idx_threshs_str.append(str(idx_thresh) + " C")
                    else:
                        for idx_thresh in idx_threshs:
                            idx_threshs_str.append(str(idx_thresh + 273.15) + " K")

                # Indices ----------------------------------------------------------------------------------------------

                # Below, unit conversion should not be required. The unit in the file produced by the scenario workflow
                # is "degree_C", but it should be "C". Ideally, this would be fixed, but it's not a major issue.

                # Number of days where daily maximum temperature exceed a threshold.
                ds_idx = None
                if idx_name == cfg.idx_tx_days_above:
                    ds_scen_tasmax = ds_scen[0][cfg.var_cordex_tasmax]
                    if rcp == "ref":
                        ds_scen_tasmax["units"] = "C"
                        ds_scen_tasmax.attrs["units"] = "C"
                    idx_thresh_str_tasmax = idx_threshs_str[0]
                    ds_idx = indices.tx_days_above(ds_scen_tasmax, idx_thresh_str_tasmax)

                # Subset based on dates.
                ds_idx_ref = ds_idx.sel(time=slice(dates_ref[0], dates_ref[1]))
                ds_idx_fut = None
                if rcp == "ref":
                    ds_idx_ref = ds_idx_ref.isel(lon=0, lat=0)
                else:
                    ds_idx_fut = ds_idx.sel(time=slice(dates_fut[0], dates_fut[1]))

                # Convert to a specific time format.
                year_1 = int(str(ds_idx_ref["time"][0].values)[0:4])
                year_n = int(str(ds_idx_ref["time"][len(ds_idx_ref['time'])-1].values)[0:4])
                ds_idx_ref["time"] = pd.date_range(str(year_1)+"-01-01", periods=year_n-year_1+1, freq="YS")
                if rcp != "ref":
                    ds_idx_fut['time'] = pd.date_range(dates_fut[0], periods=n_years_fut, freq="YS")

                # Calculate minimum, maximum and mean values.
                if ds_idx_ref_min is None:
                    ds_idx_ref_min = ds_idx_ref
                    ds_idx_ref_max = ds_idx_ref
                    ds_idx_ref_mean = ds_idx_ref / n_sim
                    if rcp != "ref":
                        ds_idx_fut_min = ds_idx_fut
                        ds_idx_fut_max = ds_idx_fut
                        ds_idx_fut_mean = ds_idx_fut / n_sim
                else:
                    def set_lon_lat(ds, lon, lat):
                        ds["lon"] = lon
                        ds["lat"] = lat
                        return ds
                    ds_idx_ref_min = xr.ufuncs.minimum(ds_idx_ref_min, ds_idx_ref)
                    ds_idx_ref_max = xr.ufuncs.maximum(ds_idx_ref_max, ds_idx_ref)
                    ds_idx_ref_mean = ds_idx_ref_mean + ds_idx_ref / n_sim
                    lon_lat = [ds_idx_ref["lon"], ds_idx_ref["lat"]]
                    set_lon_lat(ds_idx_ref_min, lon_lat[0], lon_lat[1])
                    set_lon_lat(ds_idx_ref_max, lon_lat[0], lon_lat[1])
                    set_lon_lat(ds_idx_ref_mean, lon_lat[0], lon_lat[1])
                    if rcp != "ref":
                        if ds_idx_fut_min is None:
                            ds_idx_fut_min = ds_idx_fut
                            ds_idx_fut_max = ds_idx_fut
                            ds_idx_fut_mean = ds_idx_fut / n_sim
                        else:
                            ds_idx_fut_min = xr.ufuncs.minimum(ds_idx_fut_min, ds_idx_fut)
                            ds_idx_fut_max = xr.ufuncs.maximum(ds_idx_fut_max, ds_idx_fut)
                            ds_idx_fut_mean = ds_idx_fut_mean + ds_idx_fut / n_sim
                            lon_lat = [ds_idx_fut["lon"], ds_idx_fut["lat"]]
                            set_lon_lat(ds_idx_fut_min, lon_lat[0], lon_lat[1])
                            set_lon_lat(ds_idx_fut_max, lon_lat[0], lon_lat[1])
                            set_lon_lat(ds_idx_fut_mean, lon_lat[0], lon_lat[1])

            # Combine statistics into an array (for each RCP).
            ds_ref = [ds_idx_ref_mean, ds_idx_ref_min, ds_idx_ref_max]
            if rcp != "ref":
                ds_fut = [ds_idx_fut_mean, ds_idx_fut_min, ds_idx_fut_max]
                if rcp == cfg.rcp_26:
                    ds_rcp_26 = ds_fut
                elif rcp == cfg.rcp_45:
                    ds_rcp_45 = ds_fut
                elif rcp == cfg.rcp_85:
                    ds_rcp_85 = ds_fut

            # Create NetCDF files.
            utils.log("Generating NetCDF files containing indices.", True)
            p_sim_format = cfg.get_d_sim(stn, cfg.cat_regrid, "") + idx_name + "/" + idx_name +\
                           "_<rcp>_<stat>_4qqmap.nc"
            dir_out = os.path.dirname(p_sim_format)
            if not (os.path.isdir(dir_out)):
                os.makedirs(dir_out)
            if rcp == "ref":
                p_sim_ref = p_sim_format.replace("<rcp>", rcp)
                utils.save_dataset(ds_idx_ref_mean, p_sim_ref.replace("<stat>", "mean"))
            else:
                p_sim_ref = p_sim_format.replace("<rcp>", "ref")
                utils.save_dataset(ds_idx_ref_min, p_sim_ref.replace("<stat>", "min"))
                utils.save_dataset(ds_idx_ref_max, p_sim_ref.replace("<stat>", "max"))
                p_sim_fut = p_sim_format.replace("<rcp>", rcp)
                utils.save_dataset(ds_idx_fut_min, p_sim_fut.replace("<stat>", "min"))
                utils.save_dataset(ds_idx_fut_max, p_sim_fut.replace("<stat>", "max"))
                utils.save_dataset(ds_idx_fut_mean, p_sim_fut.replace("<stat>", "mean"))

            # DEBUG: Calculate mean values.
            for years_hor in cfg.per_hors:
                dates_hor = [str(years_hor[0]) + "-01-01", str(years_hor[1]) + "-12-31"]
                val = -1.0
                if rcp == "ref":
                    val = ds_idx_ref.sel(time=slice(dates_ref[0], dates_ref[1])).mean()
                else:
                    val = ds_idx_fut.sel(time=slice(dates_hor[0], dates_hor[1])).mean()

            # Generate plot.
            if rcp == rcps[len(rcps) - 1]:
                utils.log("Generating time series of indices.", True)
                p_fig = cfg.get_d_sim(stn, cfg.cat_fig + "/indices", "") + idx_name + "_" + stn + ".png"
                plot.plot_idx_ts(ds_ref, ds_rcp_26, ds_rcp_45, ds_rcp_85, stn.capitalize(), idx_name, idx_threshs, rcps,
                                     [years_ref[0], years_fut[1]], p_fig)


def calc_idx_heatmap(idx_name, idx_threshs, rcp, per_hors):

    """
    --------------------------------------------------------------------------------------------------------------------
    Interpolate data within a zone.

    Parameters
    ----------
    idx_name: str
        Climate index.
    idx_threshs: [float]
        Climate index thresholds.
    rcp: str
        Emission scenario.
    per_hors: [[int,int]]
        Horizons.
    --------------------------------------------------------------------------------------------------------------------
    """

    utils.log("-", True)
    utils.log("Index             : " + idx_name, True)
    utils.log("Emission scenario : " + cfg.get_rcp_desc(rcp), True)
    utils.log("-", True)

    # Number of years and stations.
    if rcp == "ref":
        n_year = cfg.per_ref[1] - cfg.per_ref[0] + 1
    else:
        n_year = cfg.per_fut[1] - cfg.per_ref[1] + 1
    n_stn = len(cfg.stns)

    # Determine variable.
    var = ""
    stat = "mean"
    if idx_name == cfg.idx_tx_days_above:
        var = cfg.var_cordex_tasmax

    # Collect values for each station and determine overall boundaries.
    utils.log("Collecting emissions scenarios at all stations.", True)
    x_bnds = []
    y_bnds = []
    data_stn = []
    for stn in cfg.stns:

        # Load dataset.
        p_stn = cfg.get_d_sim(stn, "regrid/" + idx_name) + idx_name + "_" + rcp + "_" + stat + "_4qqmap.nc"
        if not(os.path.exists(p_stn)):
            continue
        ds = xr.open_dataset(p_stn)

        # Extract data from stations.
        data = [[], [], []]
        n = ds.dims["time"]
        for year in range(0, n):

            # Collect data.
            x = ds["lon"].values.ravel()[0]
            y = ds["lat"].values.ravel()[0]
            z = ds[var][year]
            if (idx_name == cfg.idx_tx_days_above) and math.isnan(z):
                z = 0
            data[0].append(x)
            data[1].append(y)
            data[2].append(int(z))

            # Update overall boundaries (round according to the variable 'step').
            if x_bnds == []:
                x_bnds = [x, x]
                y_bnds = [y, y]
            else:
                x_bnds = [min(x_bnds[0], x), max(x_bnds[1], x)]
                y_bnds = [min(y_bnds[0], y), max(y_bnds[1], y)]

        # Add data from station to complete dataset.
        data_stn.append(data)

    # Build the list of x and y locations for which interpolation is needed.
    utils.log("Collecting the coordinates of stations.", True)
    grid_time = range(0, n_year)
    def round_to_nearest_decimal(val, step):
        if val < 0:
            val_rnd = math.floor(val/step) * step
        else:
            val_rnd = math.ceil(val/step) * step
        return val_rnd
    for i in range(0, 2):
        x_bnds[i] = round_to_nearest_decimal(x_bnds[i], cfg.resol_idx)
        y_bnds[i] = round_to_nearest_decimal(y_bnds[i], cfg.resol_idx)
    grid_x = np.arange(x_bnds[0], x_bnds[1] + cfg.resol_idx, cfg.resol_idx)
    grid_y = np.arange(y_bnds[0], y_bnds[1] + cfg.resol_idx, cfg.resol_idx)

    # Perform interpolation.
    # There is a certain flexibility regarding the number of years in a dataset. Ideally, the station should not have
    # been considered in the analysis, unless there is no better option.
    utils.log("Performing interpolation.", True)
    new_grid = np.meshgrid(grid_x, grid_y)
    new_grid_data = np.empty((n_year, len(grid_y), len(grid_x)))
    for i_year in range(0, n_year):
        arr_x = []
        arr_y = []
        arr_z = []
        for i_stn in range(len(data_stn)):
            if i_year < len(data_stn[i_stn][0]):
                arr_x.append(data_stn[i_stn][0][i_year])
                arr_y.append(data_stn[i_stn][1][i_year])
                arr_z.append(data_stn[i_stn][2][i_year])
        new_grid_data[i_year, :, :] = griddata((arr_x, arr_y), arr_z, (new_grid[0], new_grid[1]), fill_value=np.nan,
                                               method="linear")
    new_data = xr.DataArray(new_grid_data,
                            coords={"time": grid_time, "lat": grid_y, "lon": grid_x},
                            dims=["time", "lat", "lon"])
    ds_regrid = new_data.to_dataset(name=idx_name)

    # Clip to country boundaries.
    if cfg.d_bounds != "":
        ds_regrid = subset.subset_shape(ds_regrid, cfg.d_bounds)

    # Loop through horizons.
    utils.log("Generating maps.", True)
    for per_hor in per_hors:

        # Select years.
        if rcp == "ref":
            year_1 = 0
            year_n = cfg.per_ref[1] - cfg.per_ref[0]
        else:
            year_1 = per_hor[0] - cfg.per_ref[1]
            year_n = per_hor[1] - cfg.per_ref[1]
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            ds_hor = ds_regrid[cfg.idx_tx_days_above][year_1:(year_n+1)][:][:].mean("time", skipna=True)

        # Plot.
        p_fig = cfg.get_d_sim("", cfg.cat_fig + "/indices", "") +\
                idx_name + "_" + rcp + "_" + str(per_hor[0]) + "_" + str(per_hor[1]) + ".png"
        plot.plot_idx_heatmap(ds_hor, idx_name, idx_threshs, grid_x, grid_y, per_hor, p_fig, "matplotlib")


def run():

    """
    --------------------------------------------------------------------------------------------------------------------
    Entry point.
    --------------------------------------------------------------------------------------------------------------------
    """

    # Calculate indices.
    utils.log("=")
    utils.log("Step #6a  Calculation of indices.")
    for i in range(0, len(cfg.idx_names)):

        # Parameters.
        idx_name = cfg.idx_names[i]
        idx_threshs = cfg.idx_threshs[i]

        # Calculate index.
        calc_idx_ts(idx_name, idx_threshs)

    # Map indices.
    # Interpolation requires multiples stations.
    utils.log("=")
    utils.log("Step #6b  Generation of index maps.")
    if len(cfg.stns) > 1:
        for i in range(0, len(cfg.idx_names)):

            # Parameters.
            idx_name = cfg.idx_names[i]
            idx_threshs = cfg.idx_threshs[i]

            # Reference period.
            calc_idx_heatmap(idx_name, idx_threshs, "ref", [cfg.per_ref])

            # Future period.
            for rcp in cfg.rcps:
                calc_idx_heatmap(idx_name, idx_threshs, rcp, cfg.per_hors)


if __name__ == "__main__":
    run()
