# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Plot functions.
#
# Authors:
# 1. rousseau.yannick@ouranos.ca
# 2. marc-andre.bourgault@ggr.ulaval.ca (original)
# (C) 2020 Ouranos, Canada
# ----------------------------------------------------------------------------------------------------------------------

import config as cfg
import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as poly
import pandas as pd
import os.path
import seaborn as sns
import utils
import xarray as xr
from scipy import signal


def plot_year(ds_hour, ds_day, set_name, var):

    """
    --------------------------------------------------------------------------------------------------------------------
    Time series.

    Parameters
    ----------
    ds_hour : xarray
        Dataset with hourly frequency.
    ds_day : xarray
        Dataset with daily frequency.
    set_name : str
        Set name.
    var : str
        Variable.
    --------------------------------------------------------------------------------------------------------------------
    """

    var_desc_unit = cfg.get_var_desc(var, set_name)  + " [" + cfg.get_var_unit(var, set_name) + "]"

    fs = 10
    f = plt.figure(figsize=(10, 3))
    f.suptitle("Comparison entre les données horaires et agrégées", fontsize=fs)

    plt.subplots_adjust(top=0.9, bottom=0.20, left=0.10, right=0.98, hspace=0.30, wspace=0.416)
    ds_hour.plot(color="black")
    plt.title("")
    plt.xlabel("", fontsize=fs)
    plt.ylabel(var_desc_unit, fontsize=fs)

    ds_day.plot(color="orange")
    plt.title("")
    plt.xlabel("", fontsize=fs)
    plt.ylabel(var_desc_unit, fontsize=fs)

    plt.close()


def plot_dayofyear(ds_day, set_name, var, date):

    """
    --------------------------------------------------------------------------------------------------------------------
    Map.

    Parameters
    ----------
    ds_day : xarray
        Dataset with daily frequency.
    set_name : str
        Set name.
    var : str
        Variable.
    date : str
        Date.
    --------------------------------------------------------------------------------------------------------------------
    """

    # Variable.
    var_desc = cfg.get_var_desc(var, set_name) + " (" + cfg.get_var_unit(var, set_name) + ")"

    # Data.
    ds_day_sel = ds_day.sel(time=date)

    # Plot.
    fs = 10
    ds_day_sel.plot.pcolormesh(add_colorbar=True, add_labels=True,
                               cbar_kwargs=dict(orientation='vertical', pad=0.05, shrink=1, label=var_desc))
    plt.title(date)
    plt.suptitle("", fontsize=fs)
    plt.xlabel("Longitude (º)", fontsize=fs)
    plt.ylabel("Latitude (º)", fontsize=fs)
    plt.tick_params(axis="x", labelsize=fs)
    plt.tick_params(axis="y", labelsize=fs)

    plt.close()


def plot_ts_single(stn, var):

    """
    --------------------------------------------------------------------------------------------------------------------
    Verify all simulations (one simulation: one plot).

    Parameters:
    ----------
    stn: str
        Station name.
    var: str
        Weather variable.
    --------------------------------------------------------------------------------------------------------------------
    """

    utils.log("Processing (single): variable = " + var + "; station = " + stn, True)

    # Weather variable description and unit.
    var_desc = cfg.get_var_desc(var)
    var_unit = cfg.get_var_unit(var)

    # Paths and NetCDF files.
    d_regrid = cfg.get_d_sim(stn, cfg.cat_regrid, var)
    p_list   = utils.list_files(d_regrid)
    p_obs    = cfg.get_p_obs(stn, var)

    # Plot.
    fs_title  = 8
    fs_legend = 8
    fs_axes   = 8

    f = plt.figure(figsize=(15, 3))
    f.add_subplot(111)
    plt.subplots_adjust(top=0.9, bottom=0.18, left=0.04, right=0.99, hspace=0.695, wspace=0.416)

    # Loop through simulation sets.
    for i in range(int(len(p_list) / 3)):

        p_ref   = [i for i in p_list if "ref" in i][i]
        p_fut   = p_ref.replace("ref_", "")
        p_qqmap = p_fut.replace("_4qqmap", "").replace(cfg.cat_regrid, cfg.cat_qqmap)
        ds_fut   = xr.open_dataset(p_fut)
        ds_qqmap = xr.open_dataset(p_qqmap)
        ds_obs   = xr.open_dataset(p_obs)

        # Convert date format if the need is.
        if ds_fut.time.dtype == cfg.dtype_obj:
            ds_fut["time"] = fix_calendar(ds_fut)
        if ds_qqmap.time.dtype == cfg.dtype_obj:
            ds_qqmap["time"] = fix_calendar(ds_qqmap)

        # Curves.
        (ds_obs[var]).plot(alpha=0.5)
        (ds_fut[var]).plot()
        (ds_qqmap[var]).plot(alpha=0.5)

        # Format.
        plt.legend(["sim", cfg.cat_qqmap, cfg.cat_obs], fontsize=fs_legend)
        title = os.path.basename(p_fut).replace("4qqmap.nc", "verif_ts_single")
        plt.suptitle(title, fontsize=fs_title)
        plt.xlabel("Année", fontsize=fs_axes)
        plt.ylabel(var_desc + " [" + var_unit + "]", fontsize=fs_axes)
        plt.title("")
        plt.suptitle(title, fontsize=fs_title)
        plt.tick_params(axis='x', labelsize=fs_axes)
        plt.tick_params(axis='y', labelsize=fs_axes)

        # Save plot.
        if cfg.opt_plt_save:
            p_fig = cfg.get_d_sim(stn, cfg.cat_fig + "/verif/ts_single", var) + title + ".png"
            utils.save_plot(plt, p_fig)

        # Close plot.
        if cfg.opt_plt_close:
            plt.close()


def plot_ts_mosaic(stn, var):

    """
    --------------------------------------------------------------------------------------------------------------------
    Verify all simulations (all in one plot).

    Parameters:
    ----------
    stn: str
        Station name.
    var: str
        Weather variable.
    --------------------------------------------------------------------------------------------------------------------
    """

    utils.log("Processing (mosaic): variable = " + var + "; station = " + stn, True)

    # Weather variable description and unit.
    var_desc = cfg.get_var_desc(var)
    var_unit = cfg.get_var_unit(var)

    # Conversion coefficient.
    coef = 1
    if var == cfg.var_cordex_pr:
        coef = cfg.spd

    # Paths and NetCDF files.
    d_regrid = cfg.get_d_sim(stn, cfg.cat_regrid, var)
    p_list   = utils.list_files(d_regrid)
    p_obs    = cfg.get_p_obs(stn, var)

    # Plot.
    fs_title  = 8
    fs_title  = 6
    fs_legend = 6
    fs_axes   = 6
    plt.figure(figsize=(15, 15))
    plt.subplots_adjust(top=0.96, bottom=0.07, left=0.04, right=0.99, hspace=0.40, wspace=0.30)

    # Loop through simulation sets.
    title = ""
    for i in range(int(len(p_list) / 3)):

        # NetCDF files.
        p_fut_i   = [i for i in p_list if "ref" in i][i].replace("ref_", "")
        p_qqmap_i = p_fut_i.replace("_4" + cfg.cat_qqmap, "").replace(cfg.cat_regrid, cfg.cat_qqmap)

        # Open datasets.
        ds_fut   = xr.open_dataset(p_fut_i)
        ds_qqmap = xr.open_dataset(p_qqmap_i)
        ds_obs   = xr.open_dataset(p_obs)

        # Convert date format if the need is.
        if ds_fut.time.dtype == cfg.dtype_obj:
            ds_fut["time"] = fix_calendar(ds_fut)
        if ds_qqmap.time.dtype == cfg.dtype_obj:
            ds_qqmap["time"] = fix_calendar(ds_qqmap)

        # Curves.
        plt.subplot(7, 7, i + 1)
        (ds_fut[var] * coef).plot()
        (ds_qqmap[var] * coef).plot(alpha=0.5)
        (ds_obs[var] * coef).plot(alpha=0.5)

        # Format.
        plt.xlabel("", fontsize=fs_axes)
        plt.ylabel(var_desc + " [" + var_unit + "]", fontsize=fs_axes)
        title = os.path.basename(p_list[i]).replace(".nc", "")
        plt.title(title, fontsize=fs_title)
        plt.tick_params(axis='x', labelsize=fs_axes)
        plt.tick_params(axis='y', labelsize=fs_axes)
        if i == 0:
            plt.legend(["sim", cfg.cat_qqmap, cfg.cat_obs], fontsize=fs_legend)
            sup_title = title + "_verif_ts_mosaic"
            plt.suptitle(sup_title, fontsize=fs_title)

    # Save plot.
    if cfg.opt_plt_save:
        p_fig = cfg.get_d_sim(stn, cfg.cat_fig + "/verif/ts_mosaic", var) + title + ".png"
        utils.save_plot(plt, p_fig)

    # Close plot.
    if cfg.opt_plt_close:
        plt.close()


def plot_monthly(stn, var):

    """
    --------------------------------------------------------------------------------------------------------------------
    Verify all simulations (all in one plot).

    Parameters:
    ----------
    stn: str
        Station name.
    var: str
        Weather variable.
    --------------------------------------------------------------------------------------------------------------------
    """

    utils.log("Processing (monthly): variable = " + var + "; station = " + stn, True)

    # Weather variable description and unit.
    var_desc = cfg.get_var_desc(var)
    var_unit = cfg.get_var_unit(var)

    # NetCDF files.
    d_regrid = cfg.get_d_sim(stn, cfg.cat_regrid, var)
    p_list   = utils.list_files(d_regrid)
    p_obs    = cfg.get_p_obs(stn, var)
    ds_obs   = xr.open_dataset(p_obs)
    ds_plt   = ds_obs.sel(time=slice("1980-01-01", "2010-12-31")).resample(time="M").mean().groupby("time.month").\
               mean()[var]

    # Plot.
    fs_title  = 8
    fs_title  = 6
    fs_legend = 6
    fs_axes   = 6
    plt.figure(figsize=(15, 15))
    plt.subplots_adjust(top=0.96, bottom=0.07, left=0.04, right=0.99, hspace=0.40, wspace=0.30)

    # Loop through simulation sets.
    sup_title = ""
    for i in range(int(len(p_list) / 3)):

        # Plot.
        plt.subplot(7, 7, i + 1)

        # Curves.
        ds = xr.open_dataset(p_list[i])[var]
        if isinstance(ds.time[0].values, np.datetime64):
            ds.sel(time=slice("1980-01-01", "2010-12-31")).resample(time="M").mean().groupby("time.month").mean().\
                plot(color="blue")
        ds = xr.open_dataset(p_list[i])[var]
        if isinstance(ds.time[0].values, np.datetime64):
            ds.sel(time=slice("2050-01-01", "2070-12-31")).resample(time="M").mean().groupby("time.month").mean().\
                plot(color="green")
        ds_plt.plot(color="red")

        # Format.
        plt.xlim([1, 12])
        plt.xticks(np.arange(1, 13, 1))
        plt.xlabel("Mois", fontsize=fs_axes)
        plt.ylabel(var_desc + " [" + var_unit + "]", fontsize=fs_axes)
        title = os.path.basename(p_list[i]).replace(".nc", "")
        plt.title(title, fontsize=fs_title)
        plt.tick_params(axis='x', labelsize=fs_axes)
        plt.tick_params(axis='y', labelsize=fs_axes)
        if i == 0:
            sup_title = title + "_verif_monthly"
            plt.suptitle(sup_title, fontsize=fs_title)

    # Format.
    plt.legend(["sim", cfg.cat_qqmap, cfg.cat_obs], fontsize=fs_legend)

    # Save plot.
    if cfg.opt_plt_save:
        p_fig = cfg.get_d_sim(stn, cfg.cat_fig + "/verif/monthly", var) + sup_title + ".png"
        utils.save_plot(plt, p_fig)

    # Close plot.
    if cfg.opt_plt_close:
        plt.close()


def plot_idx_ts(ds_ref, ds_rcp_26, ds_rcp_45, ds_rcp_85, stn, idx_name, idx_threshs, rcps, xlim, p_fig):

    """
    --------------------------------------------------------------------------------------------------------------------
    Generate a time series of a climate index for the reference period and for emission scenarios.

    Parameters
    ----------
    ds_ref : xarray[]
        Dataset for the reference period.
    ds_rcp_26 : xarray[]
        Dataset for RCP 2.6.
    ds_rcp_45 : xarray[]
        Dataset for RCP 4.5.
    ds_rcp_85 : xarray[]
        Dataset for RCP 8.5.
    stn : str
        Station name.
    idx_name : str
        Index name.
    idx_threshs : float[]
        Threshold value associated with 'var'.
    rcps : [str]
        Emission scenarios.
    xlim : [int]
        Minimum and maximum values along the x-axis.
    p_fig : str
        Path of output figure.
    --------------------------------------------------------------------------------------------------------------------
    """

    # Variable-specific treatment.
    title = ""
    if idx_name == cfg.idx_tx_days_above:
        title = "Nombre de jours avec " + cfg.get_var_desc(cfg.var_cordex_tasmax).lower() + " > " +\
                str(idx_threshs[0]) + " " + cfg.get_var_unit(cfg.var_cordex_tasmax) + " (" + stn + ")"

    # Initialize plot.
    f, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel('Année')
    ax.secondary_yaxis('right')
    ax.get_yaxis().tick_right()
    ax.axes.get_yaxis().set_visible(False)
    secax = ax.secondary_yaxis('right')
    secax.set_ylabel("Nombre de jours")
    plt.subplots_adjust(top=0.925, bottom=0.10, left=0.03, right=0.90, hspace=0.30, wspace=0.416)

    # Update plot.
    ds_ref_curve = None
    ds_ref_min = None
    ds_ref_max = None
    ds_fut_curve = None
    ds_fut_min = None
    ds_fut_max = None
    for rcp in rcps:

        color = "black"
        if rcp == "ref":
            ds_ref_curve = ds_ref[0]
            ds_ref_min   = ds_ref[1]
            ds_ref_max   = ds_ref[2]
        elif rcp == cfg.rcp_26:
            ds_fut_curve = ds_rcp_26[0]
            ds_fut_min   = ds_rcp_26[1]
            ds_fut_max   = ds_rcp_26[2]
            color = "blue"
        elif rcp == cfg.rcp_45:
            ds_fut_curve = ds_rcp_45[0]
            ds_fut_min   = ds_rcp_45[1]
            ds_fut_max   = ds_rcp_45[2]
            color = "green"
        elif rcp == cfg.rcp_85:
            ds_fut_curve = ds_rcp_85[0]
            ds_fut_min   = ds_rcp_85[1]
            ds_fut_max   = ds_rcp_85[2]
            color = "red"

        if rcp == "ref":
            ax.plot(ds_ref_max["time"], ds_ref_curve, color=color, alpha=1.0)
        else:
            ax.fill_between(ds_ref_max["time"], ds_ref_min, ds_ref_max, color="grey", alpha=0.25)
            ax.plot(ds_fut_max["time"], ds_fut_curve, color=color, alpha=1.0)
            ax.fill_between(ds_fut_max["time"], ds_fut_min, ds_fut_max, color=color, alpha=0.25)

    # Finalize plot.
    legend_list = ["Référence"]
    if cfg.rcp_26 in rcps:
        legend_list.append("RCP 2,6")
    if cfg.rcp_45 in rcps:
        legend_list.append("RCP 4,5")
    if cfg.rcp_85 in rcps:
        legend_list.append("RCP 8,5")
    ax.legend(legend_list, loc="upper left", frameon=False)
    plt.xlim(xlim[0] * 365, xlim[1] * 365)
    plt.ylim(bottom=0)

    # Save figure.
    if cfg.opt_plt_save and (p_fig != ""):
        utils.save_plot(plt, p_fig)

    plt.close()


def plot_idx_heatmap(ds, idx_name, idx_threshs, grid_x, grid_y, per, p_fig, map_package):

    """
    --------------------------------------------------------------------------------------------------------------------
    Generate a heat map of a climate index for the reference period and for emission scenarios.
    TODO: Add a color scale that is common to all horizons.

    Parameters
    ----------
    ds: xarray
        Dataset (with 2 dimensions: longitude and latitude).
    idx_name : str
        Index name.
    idx_threshs : float[]
        Threshold value associated with 'var'.
    grid_x: [float]
        X-coordinates.
    grid_y: [float]
        Y-coordinates.
    per: [int, int]
        Period of interest, for instance, [1981, 2010].
    p_fig : str
        Path of output figure.
    map_package: str
        Map package: {"seaborn", "matplotlib"}
    --------------------------------------------------------------------------------------------------------------------
    """

    title = ""
    label = ""
    if idx_name == cfg.idx_tx_days_above:
        title = "Nombre de jours avec " + cfg.get_var_desc(cfg.var_cordex_tasmax).lower() + " > " +\
                str(idx_threshs[0]) + " " + cfg.get_var_unit(cfg.var_cordex_tasmax) +\
                " (" + cfg.country.capitalize() + ", " + str(per[0]) + "-" + str(per[1]) + ")"
        label = "Nombre de jours"
    plt.subplots_adjust(top=0.9, bottom=0.11, left=0.12, right=0.995, hspace=0.695, wspace=0.416)

    # Using seaborn.
    if map_package == "seaborn":
        sns.set()
        fig, ax = plt.subplots(figsize=(8, 5))
        g = sns.heatmap(ax=ax, data=ds, xticklabels=grid_x, yticklabels=grid_y)
        x_labels = ['{:,.2f}'.format(i) for i in grid_x]
        y_labels = ['{:,.2f}'.format(i) for i in grid_y]
        g.set_xticklabels(x_labels)
        g.set_yticklabels(y_labels)

    # Using matplotlib.
    elif map_package == "matplotlib":
        fs = 10
        ds.plot.pcolormesh(add_colorbar=True, add_labels=True,
                           cbar_kwargs=dict(orientation='vertical', pad=0.05, shrink=1, label=label))
        plt.title(title)
        plt.suptitle("", fontsize=fs)
        plt.xlabel("Longitude (º)", fontsize=fs)
        plt.ylabel("Latitude (º)", fontsize=fs)
        plt.tick_params(axis="x", labelsize=fs)
        plt.tick_params(axis="y", labelsize=fs)

    # Save figure.
    if cfg.opt_plt_save and (p_fig != ""):
        utils.save_plot(plt, p_fig)

    plt.close()


def plot_ref_fut(var, nq, up_qmf, time_int, p_regrid_ref, p_regrid_fut, p_fig):

    """
    --------------------------------------------------------------------------------------------------------------------
    Generates a plot of reference and future periods.

    Parameters
    ----------
    var : str
        Weather var.
    nq : int
        ...
    up_qmf : float
        ...
    time_int : int
        ...
    p_regrid_ref : str
        Path of the NetCDF file containing data for the reference period.
    p_regrid_fut : str
        Path of the NetCDF file containing data for the future period.
    p_fig : str
        Path of output figure.
    --------------------------------------------------------------------------------------------------------------------
    """

    # Weather variable description and unit.
    var_desc = cfg.get_var_desc(var)
    var_unit = cfg.get_var_unit(var)

    # Load datasets.
    ds_ref = xr.open_dataset(p_regrid_ref)[var]
    ds_fut = xr.open_dataset(p_regrid_fut)[var]

    # Fit.
    x     = [*range(len(ds_ref.time))]
    y     = ds_ref.values
    coefs = poly.polyfit(x, y, 4)
    ffit  = poly.polyval(x, coefs)

    # Initialize plot.
    fs_sup_title = 8
    fs_title     = 8
    fs_legend    = 6
    fs_axes      = 8
    f = plt.figure(figsize=(15, 6))
    f.add_subplot(211)
    plt.subplots_adjust(top=0.90, bottom=0.07, left=0.04, right=0.99, hspace=0.40, wspace=0.00)
    sup_title = os.path.basename(p_fig).replace(".png", "") +\
                "_time_int_" + str(time_int) + "_up_qmf_" + str(up_qmf) + "_nq_" + str(nq)
    plt.suptitle(sup_title, fontsize=fs_sup_title)

    # Convert date format if the need is.
    if ds_ref.time.dtype == cfg.dtype_obj:
        ds_ref["time"] = fix_calendar(ds_ref)

    # Upper plot: Reference period.
    f.add_subplot(211)
    plt.plot(ds_ref.time, y)
    plt.plot(ds_ref.time, ffit)
    plt.legend(["référence", "tendance"], fontsize=fs_legend)
    plt.xlabel("Année", fontsize=fs_axes)
    plt.ylabel(var_desc + " [" + var_unit + "]", fontsize=fs_axes)
    plt.tick_params(axis='x', labelsize=fs_axes)
    plt.tick_params(axis='y', labelsize=fs_axes)
    plt.title("Période de référence", fontsize=fs_title)

    # Lower plot: Complete simulation.
    f.add_subplot(212)
    plt.plot(signal.detrend(ds_fut), alpha=0.5)
    plt.plot(y - ffit, alpha=0.5)
    plt.legend(["simulation", "référence"], fontsize=fs_legend)
    plt.xlabel("Jours", fontsize=fs_axes)
    plt.ylabel(var_desc + " [" + var_unit + "]", fontsize=fs_axes)
    plt.tick_params(axis='x', labelsize=fs_axes)
    plt.tick_params(axis='y', labelsize=fs_axes)
    plt.title("Période de simulation", fontsize=fs_title)

    # Save plot.
    if cfg.opt_plt_save and (p_fig != ""):
        utils.save_plot(plt, p_fig)

    # Close plot.
    if cfg.opt_plt_close:
        plt.close()


def plot_obs_fut(ds_obs, ds_fut, var, title, p_fig):

    """
    --------------------------------------------------------------------------------------------------------------------
    Generates a plot of observed and future periods.

    Parameters
    ----------
    ds_obs : xarray
        Dataset of observed period.
    ds_fut : xarray
        Dataset of future period.
    var : str
        Variable.
    title : str
        Title of figure.
    p_fig : str
        Path of output figure.
    --------------------------------------------------------------------------------------------------------------------
    """

    # Convert date format if the need is.
    if ds_obs.time.dtype == cfg.dtype_obj:
        ds_obs["time"] = fix_calendar(ds_obs)
    if ds_fut.time.dtype == cfg.dtype_obj:
        ds_fut["time"] = fix_calendar(ds_fut)

    # Weather variable description and unit.
    var_desc = cfg.get_var_desc(var)
    var_unit = cfg.get_var_unit(var)

    # Conversion coefficient.
    coef = 1
    if var == cfg.var_cordex_pr:
        coef = cfg.spd

    fs_sup_title = 8
    fs_legend = 8
    fs_axes = 8
    f = plt.figure(figsize=(15, 3))
    f.add_subplot(111)
    plt.subplots_adjust(top=0.9, bottom=0.21, left=0.04, right=0.99, hspace=0.695, wspace=0.416)

    # Precipitation.
    (ds_fut[var] * coef).plot(alpha=0.5)
    if var == cfg.var_cordex_pr:
        (ds_obs[var] * coef).plot()
    # Other variables.
    else:
        ds_obs[var].plot()
    plt.legend(["sim", "obs"], fontsize=fs_legend)
    plt.xlabel("Année", fontsize=fs_axes)
    plt.ylabel(var_desc + " [" + var_unit + "]", fontsize=fs_axes)
    plt.title("")
    plt.suptitle(title, fontsize=fs_sup_title)
    plt.tick_params(axis='x', labelsize=fs_axes)
    plt.tick_params(axis='y', labelsize=fs_axes)

    # Save plot.
    if cfg.opt_plt_save and (p_fig != ""):
        utils.save_plot(plt, p_fig)

    # Close plot.
    if cfg.opt_plt_close:
        plt.close()


def plot_postprocess_fut_obs(ds_obs, ds_fut, ds_qqmap, var, p_fig, title):

    """
    --------------------------------------------------------------------------------------------------------------------
    Generates a plot of observed and future periods.

    Parameters
    ----------
    ds_obs : xarray
        Dataset of observed period.
    ds_fut : xarray
        Dataset of future period.
    var : str
        Variable.
    title : str
        Title of figure.
    p_fig : str
        Path of output figure.
    --------------------------------------------------------------------------------------------------------------------
    """

    # Weather variable description and unit.
    var_desc = cfg.get_var_desc(var)
    var_unit = cfg.get_var_unit(var)

    # Conversion coefficient.
    coef = 1
    if var == cfg.var_cordex_pr:
        coef = cfg.spd

    # Plot.
    f = plt.figure(figsize=(15, 3))
    f.add_subplot(111)
    plt.subplots_adjust(top=0.9, bottom=0.15, left=0.04, right=0.99, hspace=0.695, wspace=0.416)
    fs_sup_title = 8
    fs_legend = 8
    fs_axes = 8
    legend = ["sim", cfg.cat_obs]
    if ds_qqmap is not None:
        legend.insert(0, "pp")
        (ds_qqmap * coef).groupby(ds_qqmap.time.dt.year).mean().plot()
    (ds_fut * coef).groupby(ds_fut.time.dt.year).mean().plot()
    (ds_obs * coef).groupby(ds_obs.time.dt.year).mean().plot()
    plt.legend(legend, fontsize=fs_legend)
    plt.xlabel("Année", fontsize=fs_axes)
    plt.ylabel(var_desc + " [" + var_unit + "]", fontsize=fs_axes)
    plt.title("")
    plt.suptitle(title, fontsize=fs_sup_title)
    plt.tick_params(axis='x', labelsize=fs_axes)
    plt.tick_params(axis='y', labelsize=fs_axes)

    # Save plot.
    if cfg.opt_plt_save and (p_fig != ""):
        utils.save_plot(plt, p_fig)

    # Close plot.
    if cfg.opt_plt_close:
        plt.close()


def plot_calib_summary(ds_qmf, ds_qqmap_per, ds_obs, ds_ref, ds_fut, ds_qqmap, var, title, p_fig):

    """
    --------------------------------------------------------------------------------------------------------------------
    Generates a plot containing a summary of calibration.

    Parameters
    ----------
    ds_qmf : xarray
        Dataset of quantile mapping function.
    ds_qqmap_per : xarray
        ???
    ds_obs : xarray
        Dataset of bservations.
    ds_ref : xarray
        Dataset of reference period.
    ds_fut : xarray
        Dataset of future period.
    ds_qqmap : xarray
        Dataset of qqmap.
    var : str
        Variable.
    title : str
        Title of figure.
    p_fig : str
        Path of output figure.
    --------------------------------------------------------------------------------------------------------------------
    """

    # Weather variable description and unit.
    var_desc = cfg.get_var_desc(var)
    var_unit = cfg.get_var_unit(var)

    # Quantile ---------------------------------------------------------------------------------------------------------

    fs_sup_title = 8
    fs_title     = 6
    fs_legend    = 4
    fs_axes      = 7

    f = plt.figure(figsize=(9, 6))
    f.add_subplot(331)
    plt.subplots_adjust(top=0.9, bottom=0.126, left=0.070, right=0.973, hspace=0.695, wspace=0.416)

    ds_qmf.plot()
    plt.xlabel("Quantile", fontsize=fs_axes)
    plt.ylabel("Jour de l'année", fontsize=fs_axes)
    plt.tick_params(axis='x', labelsize=fs_axes)
    plt.tick_params(axis='y', labelsize=fs_axes)

    # Mean annual values -----------------------------------------------------------------------------------------------

    # Plot.
    f.add_subplot(332)
    if var == cfg.var_cordex_pr:
        draw_curves(var, ds_qqmap_per, ds_obs, ds_ref, ds_fut, ds_qqmap, "sum")
    else:
        draw_curves(var, ds_qqmap_per, ds_obs, ds_ref, ds_fut, ds_qqmap, "mean")
    plt.title(var_desc, fontsize=fs_title)
    plt.legend([cfg.cat_qqmap+"-ref", "sim-ref", cfg.cat_obs, cfg.cat_qqmap+"_all", "sim-all"], fontsize=fs_legend)
    plt.xlim([1, 12])
    plt.xticks(np.arange(1, 13, 1))
    plt.xlabel("Année", fontsize=fs_axes)
    plt.ylabel(var_desc + " [" + var_unit + "]", fontsize=fs_axes)
    plt.tick_params(axis='x', labelsize=fs_axes)
    plt.tick_params(axis='y', labelsize=fs_axes)

    # Maximum, Q99, Q75 and mean monthly values ------------------------------------------------------------------------

    for i in range(1, 5):

        plt.subplot(333 + i - 1)

        title    = " (mensuel)"
        quantile = -1
        if i == 1:
            title = "Maximum" + title
        elif i == 2:
            title    = "Q99" + title
            quantile = 0.99
        elif i == 3:
            title    = "Q75" + title
            quantile = 0.75
        else:
            title = "Moyenne" + title

        if i == 1:
            draw_curves(var, ds_qqmap_per, ds_obs, ds_ref, ds_fut, ds_qqmap, "max")
        elif (i == 2) or (i == 3):
            draw_curves(var, ds_qqmap_per, ds_obs, ds_ref, ds_fut, ds_qqmap, "quantile", quantile)
        else:
            draw_curves(var, ds_qqmap_per, ds_obs, ds_ref, ds_fut, ds_qqmap, "mean")

        plt.xlim([1, 12])
        plt.xticks(np.arange(1, 13, 1))
        plt.xlabel("Mois", fontsize=fs_axes)
        plt.ylabel(var_desc + " [" + var_unit + "]", fontsize=fs_axes)
        plt.legend([cfg.cat_qqmap+"-ref", "sim-ref", cfg.cat_obs, cfg.cat_qqmap+"_all", "sim-all"], fontsize=fs_legend)
        plt.title(title, fontsize=fs_title)
        plt.tick_params(axis='x', labelsize=fs_axes)
        plt.tick_params(axis='y', labelsize=fs_axes)

    # Time series ------------------------------------------------------------------------------------------------------

    # Conversion coefficient.
    coef = 1
    if var == cfg.var_cordex_pr:
        coef = cfg.spd

    # Convert date format if the need is.
    if ds_qqmap.time.time.dtype == cfg.dtype_obj:
        ds_qqmap["time"] = fix_calendar(ds_qqmap.time)
    if ds_ref.time.time.dtype == cfg.dtype_obj:
        ds_ref["time"] = fix_calendar(ds_ref.time)

    plt.subplot(313)
    (ds_qqmap * coef).plot(alpha=0.5)
    (ds_ref * coef).plot(alpha=0.5)
    (ds_obs * coef).plot(alpha=0.5)
    if var == cfg.var_cordex_pr:
        plt.ylim([0, 300])
    # Other variables.
    else:
        pass
    plt.xlabel("Année", fontsize=fs_axes)
    plt.ylabel(var_desc + " [" + var_unit + "]", fontsize=fs_axes)
    plt.legend([cfg.cat_qqmap, "sim", cfg.cat_obs], fontsize=fs_legend)
    plt.title("")

    f.suptitle(title, fontsize=fs_sup_title)
    plt.tick_params(axis='x', labelsize=fs_axes)
    plt.tick_params(axis='y', labelsize=fs_axes)

    del ds_qqmap.attrs['bias_corrected']

    # Save plot.
    if cfg.opt_plt_save and (p_fig != ""):
        utils.save_plot(plt, p_fig)

    # Close plot.
    if cfg.opt_plt_close:
        plt.close()


def draw_curves(var, ds, ds_obs, ds_ref, ds_fut, ds_qqmap, stat, quantile=-1.0):

    """
    --------------------------------------------------------------------------------------------------------------------
    Draw curves.

    Parameters
    ----------
    var : str
        Weather variable.
    ds : xarray.dataset
        ...
    ds_obs : xarray.dataset
        ...
    ds_ref : xarray.dataset
        Dataset for the reference period.
    ds_fut : xarray.dataset
        Dataset for the future period.
    ds_qqmap : xarray.dataset
        Dataset for the qqmap.
    stat : {"max", "quantile", "mean", "sum"}
        Statistic.
    quantile : float, optional
        Quantile.
    --------------------------------------------------------------------------------------------------------------------
    """

    # Conversion coefficient.
    coef = 1
    if var == cfg.var_cordex_pr:
        coef = cfg.spd

    # Draw curves.
    if stat == "max":
        (ds * coef).groupby(ds.time.dt.month).max().plot()
        (ds_ref * coef).groupby(ds_ref.time.dt.month).max().plot()
        (ds_obs * coef).groupby(ds_obs.time.dt.month).max().plot()
        (ds_qqmap * coef).groupby(ds_qqmap.time.dt.month).max().plot()
        (ds_fut * coef).groupby(ds_fut.time.dt.month).max().plot()
    elif stat == "quantile":
        (ds * coef).groupby(ds.time.dt.month).quantile(quantile).plot()
        (ds_ref * coef).groupby(ds_ref.time.dt.month).quantile(quantile).plot()
        (ds_obs * coef).groupby(ds_obs.time.dt.month).quantile(quantile).plot()
        (ds_qqmap * coef).groupby(ds_qqmap.time.dt.month).quantile(quantile).plot()
        (ds_fut * coef).groupby(ds_fut.time.dt.month).quantile(quantile).plot()
    elif stat == "mean":
        (ds * coef).groupby(ds.time.dt.month).mean().plot()
        (ds_ref * coef).groupby(ds_ref.time.dt.month).mean().plot()
        (ds_obs * coef).groupby(ds_obs.time.dt.month).mean().plot()
        (ds_qqmap * coef).groupby(ds_qqmap.time.dt.month).mean().plot()
        (ds_fut * coef).groupby(ds_fut.time.dt.month).mean().plot()
    elif stat == "sum":
        (ds * coef).groupby(ds.time.dt.year).sum().plot()
        (ds_ref * coef).groupby(ds_ref.time.dt.year).sum().plot()
        (ds_obs * coef).groupby(ds_obs.time.dt.year).sum().plot()
        (ds_qqmap * coef).groupby(ds_qqmap.time.dt.year).sum().plot()
        (ds_fut * coef).groupby(ds_fut.time.dt.year).sum().plot()


def fix_calendar(ds):

    """
    --------------------------------------------------------------------------------------------------------------------
    Fix calendar when type is 'cfg.dtype_obj'.

    Parameters
    ----------
    ds : xarray
        Dataset.
    --------------------------------------------------------------------------------------------------------------------
    """

    year_1 = ds.time.values[0].year
    year_n = ds.time.values[len(ds.time.values) - 1].year
    new_time = pd.date_range(str(year_1) + "-01-01", periods=(year_n - year_1 + 1) * 365, freq='D')

    return new_time


def plot_360_vs_365(ds_360, ds_365, var=""):

    """
    --------------------------------------------------------------------------------------------------------------------
    Compare a 360- vs. 365-day calendars.

    Parameters
    ----------
    ds_360 : xarray
        Dataset.
    ds_365 : xarray
        Dataset.
    var : str
        Variable.
    --------------------------------------------------------------------------------------------------------------------
    """

    if var != "":
        plt.plot((np.arange(1, 361) / 360) * 365, ds_360[var][:360].values)
        plt.plot(np.arange(1, 366), ds_365[var].values[:365], alpha=0.5)
    else:
        plt.plot((np.arange(1, 361) / 360) * 365, ds_360[:360].values)
        plt.plot(np.arange(1, 366), ds_365[:365].values, alpha=0.5)
    plt.close()

def plot_rsq(rsq, n_sim):

    """
    --------------------------------------------------------------------------------------------------------------------
    Generate a plot of root mean square error.

    Parameters
    ----------
    rsq : np
        Numpy array.
    n_sim : int
        Number of simulations
    --------------------------------------------------------------------------------------------------------------------
    """

    plt.figure()
    plt.plot(range(1, n_sim + 1), rsq, "k", label="R²")
    plt.plot(np.arange(1.5, n_sim + 0.5), np.diff(rsq), "r", label="ΔR²")
    axes = plt.gca()
    axes.set_xlim([0, n_sim])
    axes.set_ylim([0, 1])
    plt.xlabel("Number of groups")
    plt.ylabel("R² / ΔR²")
    plt.legend(loc="center right")
    plt.title("R² of groups vs. full ensemble")
    plt.close()