# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# Script configuration.
#
# TODO.YR: Determine why exception lists are required (sim_excepts, var_sim_excepts). This seems to be due to calendar
#          format.

# Contributors:
# 1. rousseau.yannick@ouranos.ca
# (C) 2020 Ouranos Inc., Canada
# ----------------------------------------------------------------------------------------------------------------------


# Constants ------------------------------------------------------------------------------------------------------------

# Reanalysis data.
obs_src_era5        = "era5"        # ERA5.
obs_src_era5_land   = "era5_land"   # ERA5-Land.
obs_src_merra2      = "merra2"      # Merra2.

# Emission scenarios.
rcp_ref             = "ref"         # Reference period.
rcp_26              = "rcp26"       # Future period RCP 2.6.
rcp_45              = "rcp45"       # Future period RCP 4.5.
rcp_85              = "rcp85"       # Future period RCP 8.5.

# Data array attributes.
attrs_units         = "units"
attrs_sname         = "standard_name"
attrs_lname         = "long_name"
attrs_axis          = "axis"
attrs_gmap          = "grid_mapping"
attrs_gmapname      = "grid_mapping_name"
attrs_bias          = "bias_corrected"
attrs_comments      = "comments"
attrs_stn           = "Station Name"
attrs_group         = "group"
attrs_kind          = "kind"

# Dataset dimensions.
dim_lon       = "lon"
dim_lat       = "lat"
dim_rlon      = "rlon"
dim_rlat      = "rlat"
dim_longitude = "longitude"
dim_latitude  = "latitude"
dim_time      = "time"

# ==========================================================
# TODO.CUSTOMIZATION.BEGIN
# Add new CORDEX AND ERA5* variables below.
# ==========================================================

# Variables (cordex).
var_cordex_tas        = "tas"         # Temperature (daily mean).
var_cordex_tasmin     = "tasmin"      # Temperature (daily minimum).
var_cordex_tasmax     = "tasmax"      # Temperature (daily maximum).
var_cordex_pr         = "pr"          # Precipitation.
var_cordex_uas        = "uas"         # Wind speed, eastward.
var_cordex_vas        = "vas"         # Wind speed, northward.
var_cordex_ps         = "ps"          # Barometric pressure.
var_cordex_rsds       = "rsds"        # Solar radiation.
var_cordex_evapsbl    = "evapsbl"     # Evaporation.
var_cordex_evapsblpot = "evapsblpot"   # Potential evapotranspiration.
var_cordex_huss       = "huss"        # Specific humidity.
var_cordex_clt        = "clt"         # Cloud cover.

# Variables (era5 and era5_land).
var_era5_t2m        = "t2m"         # Temperature.
var_era5_t2mmin     = "t2mmin"      # Temperature (daily minimum).
var_era5_t2mmax     = "t2mmax"      # Temperature (daily maximum).
var_era5_tp         = "tp"          # Precipitation.
var_era5_u10        = "u10"         # Wind speed, eastward.
var_era5_v10        = "v10"         # Wind speed, northward.
var_era5_sp         = "sp"          # Barometric pressure.
var_era5_ssrd       = "ssrd"        # Solar radiation.
var_era5_e          = "e"           # Evaporation.
var_era5_pev        = "pev"         # Potential evapotranspiration.
var_era5_d2m        = "d2m"         # Dew temperature.
var_era5_sh         = "sh"          # Specific humidity.

# ==========================================================
# TODO.CUSTOMIZATION.END
# ==========================================================

# Directory names.
# Reference data.
cat_stn             = "stn"          # At-a-station or reanalysis data.
# Scenario files (in order of generation).
cat_obs             = "obs"          # Observation.
cat_raw             = "raw"          # Raw.
cat_regrid          = "regrid"       # Reggrided.
cat_qqmap           = "qqmap"        # Adjusted simulation.
cat_qmf             = "qmf"          # Quantile mapping function.
# Scenarios vs. indices.
cat_scen            = "scen"         # Scenarios.
cat_idx             = "idx"          # Indices.
# Other.
cat_stat            = "stat"         # Statistics.
cat_fig             = "fig"          # Figures.
cat_fig_calibration = "calibration"  # Figures (calibration).
cat_fig_postprocess = "postprocess"  # Figures (postprocess).
cat_fig_workflow    = "workflow"     # Figures (workflow).

# Calendar types.
cal_noleap          = "noleap"      # No-leap.
cal_360day          = "360_day"     # 360 days.
cal_365day          = "365_day"     # 365 days.

# Date type.
dtype_obj           = "object"
dtype_64            = "datetime64[ns]"

# Data frequency.
freq_D              = "D"           # Daily.
freq_YS             = "YS"          # Annual.

# Scenarios.
group               = "time.dayofyear"  # Grouping period.

# Kind.
kind_add            = "+"               # Additive.
kind_mult           = "*"               # Multiplicative.

# Calibration.
opt_calib_bias_meth_r2     = "r2"       # Coefficient of determination.
opt_calib_bias_meth_mae    = "mae"      # Mean absolute error.
opt_calib_bias_meth_rmse   = "rmse"     # Root mean square error.
opt_calib_bias_meth_rrmse  = "rrmse"    # Relative root mean square error.

# Indices.
idx_tx_days_above   = "tx_days_above"   # Number of days per year with a maximum temperature above a threshold value.

# Statistics.
stat_mean           = "mean"        # Mean value.
stat_min            = "min"         # Minimum value.
stat_max            = "max"         # Maximum value.
stat_sum            = "sum"         # Sum of values.
stat_quantile       = "quantile"    # Value associated with a given quantile.

# Numerical parameters.
spd                 = 86400         # Number of seconds per day.
d_KC                = 273.15        # Temperature difference between Kelvin and Celcius.

# Files.
file_sep            = ","           # File separator (in CSV files).

# Context --------------------------------------------------------------------------------------------------------------

# Country and project.
country             = ""            # Country name.
project             = ""            # Project acronym.

# Emission scenarios, periods and horizons.
rcps                = [rcp_26, rcp_45, rcp_85]                      # All emission scenarios.
per_ref             = [1981, 2010]                                  # Reference period.
per_fut             = [1981, 2100]                                  # Future period.
per_hors            = [[2021, 2040], [2041, 2060], [2061, 2080]]    # Horizons.

# Boundary box.
lon_bnds                = [0, 0]    # Longitude boundaries.
lat_bnds                = [0, 0]    # Latitude boundaries.

# Stations.
# Observations are located in directories /exec/<user_name>/<country>/<project>/obs/<obs_provider>/<var>/*.csv
stns                = []            # Station names.

# Reanalysis data.
obs_src             = ""            # Provider of observations or reanalysis set.
obs_src_username    = ""            # Username of account to download 'obs_src_era5' or 'obs_src_era5_land' data.
obs_src_password    = ""            # Password of account to download 'obs_src_era5' or 'obs_src_era5_land' data.

# Variables.
variables_cordex    = []            # CORDEX data.
variables_ra        = []            # Reanalysis data.
priority_timestep   = ["day"] * len(variables_cordex)

# System ---------------------------------------------------------------------------------------------------------------

# Input-only files and directories.
d_proj              = ""            # Projections.
d_ra_raw            = ""            # Reanalysis set (default frequency, usually hourly).
d_bounds            = ""            # geog.json file comprising political boundaries.
d_bounds_shp        = ""            # Shapefile comprising political boundaries.
# Output-only files and directories.
d_stn               = ""            # Observations or reanalysis.
d_res              = ""             # Results.
# Input and output files and directories.
d_exec              = ""            # Base directory #3 (stations and output).
d_ra_day            = ""            # Reanalysis set (aggregated frequency, i.e. daily).

# Log file.
p_log               = ""            # Log file (date and time).
log_n_blank         = 10            # Number of blanks at the beginning of a message.
log_sep_len         = 110           # Number of instances of the symbol "-" in a separator line.
opt_trace           = False         # If True, additional traces are enabled/logged.

# Calibration parameters file.
p_calib             = "calib.csv"   # Calibration file (bias adjustment parameters).

# Performance.
n_proc              = 1             # Number of processes (for multiprocessing).
pid                 = -1            # Process identifier (primary process)

# Step 2 - Download and aggregation ------------------------------------------------------------------------------------

# Download.
opt_download        = False         # If True, download a dataset.
variables_download  = []            # Variables to download.
lon_bnds_download   = [0, 0]        # Longitude boundaries.
lat_bnds_download   = [0, 0]        # Latitude boundaries.

# Aggregation.
opt_aggregate       = False         # If True, aggregate data.

# Steps 3-4 - Data extraction and scenarios ----------------------------------------------------------------------------

opt_ra                  = False      # If True, the analysis is based on reanalysis data.

# Scenarios.
opt_scen                = True      # If True, produce climate scenarios.
radius                  = 0.5       # Search radius (around any given location).
detrend_order           = None      # TODO.MAB: Seems to be not working.

# Patch.
# Simulation excluded from the analysis.
# Ex1: "RCA4_AFR-44_ICHEC-EC-EARTH_rcp85",
# Ex2: "RCA4_AFR-44_MPI-M-MPI-ESM-LR_rcp85",
# Ex3: "HIRHAM5_AFR-44_ICHEC-EC-EARTH_rcp45.nc",
# Ex4: "HIRHAM5_AFR-44_ICHEC-EC-EARTH_rcp85.nc"
sim_excepts = []
# Simulation-variable combinations excluded from the analysis.
# Ex1: "pr_RCA4_AFR-44_CSIRO-QCCCE-CSIRO-Mk3-6-0_rcp85.nc",
# Ex2: "tasmin_REMO2009_AFR-44_MIROC-MIROC5_rcp26.nc
var_sim_excepts = []

# Step 5 - Bias adjustment and statistical downscaling -----------------------------------------------------------------

# Calibration options.
opt_calib           = True          # If True, explores the sensitivity to nq, up_qmf and time_win parameters.
opt_calib_auto      = True          # If True, calibrates for nq, up_qmf and time_win parameters.
opt_calib_bias      = True          # If True, examines bias correction.
opt_calib_bias_meth = "rrmse"       # Error quantification method (select one of the following methods).
opt_calib_coherence = False         # If True, examines physical coherence.
opt_calib_qqmap     = True          # If true, calculate qqmap.

# Bias parameters.
# The parameter 'time_win' is the number of days before and after any given day (15 days before and after = 30 days).
# This needs to be adjusted as there is period of adjustment between cold period and monsoon). It's possible that a
# very small precipitation amount be considered extreme. We need to limit correction factors.

# Default values.
nq_default          = 50            # Default 'nq' value.
up_qmf_default      = 3.0           # Default 'up_qmf' value.
time_win_default    = 30            # Default 'time_win' value.
bias_err_default    = -1            # Default 'bias_err' value.

# Array of values to test for each calibration parameter.
nq_calib            = [nq_default]          # List of 'nq' values to test during calibration.
up_qmf_calib        = [up_qmf_default]      # List of 'up_wmf' values to test during calibration.
time_win_calib      = [time_win_default]    # List of 'time_win' values to test during calibration.
bias_err_calib      = [bias_err_default]    # List of 'bias_err' values to test during calibration.

# Container for calibration parameters ().
df_calib            = None          # Pandas dataframe.

# Step 6 - Indices -----------------------------------------------------------------------------------------------------

# Indices.
opt_idx             = True          # If True, calculate indices.
idx_resol           = 0.05          # Spatial resolution for mapping.
idx_names           = []            # Index names.
idx_threshs         = []            # Index thresholds.

# Step 7 - Statistics --------------------------------------------------------------------------------------------------

opt_stat            = True          # If True, calculate statistics.
stat_quantiles      = [1.00, 0.99, 0.75, 0.50, 0.25, 0.01, 0.00]  # Quantiles.
opt_conv_nc_csv     = False         # If True, this convert all NetCDF files to CSV files.

# Step 8 - Visualization -----------------------------------------------------------------------------------------------

# Plots.
opt_plot            = True          # If True, actives plot generation.
opt_plot_heat       = False         # If True, generate heat maps (scenarios and indices).

# Color associated with specific datasets (for consistency).
col_sim_adj_ref     = "blue"        # Simulation (bias-adjusted) for the reference period.
col_sim_ref         = "orange"      # Simulation (non-adjusted) for the reference period
col_obs             = "green"       # Observations.
col_sim_adj         = "red"         # Simulation (bias-adjusted).
col_sim_fut         = "purple"      # Simulation (non-adjusted) for the future period.
col_ref             = "black"       # Reference period.
col_rcp26           = "blue"        # RCP 2.6.
col_rcp45           = "green"       # RCP 4.5.
col_rcp85           = "red"         # RCP 8.5.


def get_rank_inst():

    """
    --------------------------------------------------------------------------------------------------------------------
    Get the token corresponding to the institute.
    --------------------------------------------------------------------------------------------------------------------
    """

    return len(d_proj.split("/"))


def get_rank_gcm():

    """
    --------------------------------------------------------------------------------------------------------------------
    Get the rank of token corresponding to the GCM.
    --------------------------------------------------------------------------------------------------------------------
    """

    return get_rank_inst() + 1


def get_var_desc(var: str, set_name: str = "cordex"):

    """
    --------------------------------------------------------------------------------------------------------------------
    Gets the description of a variable.

    Parameters
    ----------
    var : str
        Variable.
    set_name : str
        Station name.
    --------------------------------------------------------------------------------------------------------------------
    """

    var_desc = ""
    if set_name == "cordex":
        if var == var_cordex_tas:
            var_desc = "Temp. moyenne"
        elif var == var_cordex_tasmin:
            var_desc = "Temp. minimale"
        elif var == var_cordex_tasmax:
            var_desc = "Temp. maximale"
        elif var == var_cordex_ps:
            var_desc = "Pression barométrique"
        elif var == var_cordex_pr:
            var_desc = "Précipitations"
        elif var == var_cordex_rsds:
            var_desc = "Radiation solaire"
        elif var == var_cordex_uas:
            var_desc = "Vent (dir. est)"
        elif var == var_cordex_vas:
            var_desc = "Vent (dir. nord)"
        elif var == var_cordex_clt:
            var_desc = "Couvert nuageux"
        elif var == var_cordex_huss:
            var_desc = "Humidité spécifique"
    elif (set_name == obs_src_era5) or (set_name == obs_src_era5_land):
        if var == var_era5_d2m:
            var_desc = "Point de rosée"
        elif var == var_era5_t2m:
            var_desc = "Température"
        elif var == var_era5_sp:
            var_desc = "Pression barométrique"
        elif var == var_era5_tp:
            var_desc = "Précipitations"
        elif var == var_era5_u10:
            var_desc = "Vent (dir. est)"
        elif var == var_era5_v10:
            var_desc = "Vent (dir. nord)"
        elif var == var_era5_ssrd:
            var_desc = "Radiation solaire"
        elif var == var_era5_e:
            var_desc = "Évaporation"
        elif var == var_era5_pev:
            var_desc = "Évapotranspiration potentielle"
        elif var == var_era5_sh:
            var_desc = "Humidité spécifique"

    return var_desc


def get_idx_desc(idx_name: str, idx_threshs_loc: [[float]]):

    """
    ----------------------------------------------------------------------------------------------------------------
    Gets the description of an index.

    Parameters
    ----------
    idx_name : str
        Climate index.
    idx_threshs_loc : [[float]]]
        Thresholds
    ----------------------------------------------------------------------------------------------------------------
    """

    idx_desc = ""

    # ==========================================================
    # TODO.CUSTOMIZATION.BEGIN
    # When adding a new climate index, copy the following code
    # block.
    # ==========================================================

    if idx_name == idx_tx_days_above:
        idx_desc = "Nombre de jours avec " + get_var_desc(var_cordex_tasmax).lower() + " > " +\
            str(idx_threshs_loc[0])

    # ==========================================================
    # TODO.CUSTOMIZATION.END
    # ==========================================================

    return idx_desc


def convert_var_name(var: str):

    """
    --------------------------------------------------------------------------------------------------------------------
    Convert from CORDEX variable name to the equivalent in the ERA5 set (or the opposite).

    Parameters
    ----------
    var : str
        Variable.
    --------------------------------------------------------------------------------------------------------------------
    """

    # Pairs.
    pairs = [[var_cordex_tas, var_era5_t2m], [var_cordex_tasmin, var_era5_t2mmin], [var_cordex_tasmax, var_era5_t2mmax],
             [var_cordex_pr, var_era5_tp], [var_cordex_uas, var_era5_u10], [var_cordex_vas, var_era5_v10],
             [var_cordex_ps, var_era5_sp], [var_cordex_rsds, var_era5_ssrd],
             [var_cordex_evapsbl, var_era5_e], [var_cordex_evapsblpot, var_era5_pev], [var_cordex_huss, var_era5_sh]]

    # Loop through pairs.
    for i in range(len(pairs)):
        var_type_a = pairs[i][0]
        var_type_b = pairs[i][1]

        # Verify if there is a match.
        if var == var_type_a:
            return var_type_b
        elif var == var_type_b:
            return var_type_a

    return None


def get_var_unit(var: str, set_name: str = "cordex"):

    """
    --------------------------------------------------------------------------------------------------------------------
    Gets the unit of a variable.

    Parameters
    ----------
    var : str
        Variable.
    set_name : str
        Station name.
    --------------------------------------------------------------------------------------------------------------------
    """

    var_unit = ""
    if set_name == "cordex":
        if (var == var_cordex_tas) or (var == var_cordex_tasmin) or (var == var_cordex_tasmax):
            var_unit = "°C"
        elif var == var_cordex_rsds:
            var_unit = "Pa"
        elif var == var_cordex_pr:
            var_unit = "mm"
        elif (var == var_cordex_uas) or (var == var_cordex_vas):
            var_unit = "m s-1"
        elif var == var_cordex_clt:
            var_unit = "%"
        elif var == var_cordex_huss:
            var_unit = "1"
    elif (set_name == obs_src_era5) or (set_name == obs_src_era5_land):
        if (var == var_era5_d2m) or (var == var_era5_t2m):
            var_unit = "°"
        elif var == var_era5_sp:
            var_unit = "Pa"
        elif (var == var_era5_u10) or (var == var_era5_v10):
            var_unit = "m s-1"
        elif var == var_era5_ssrd:
            var_unit = "J m-2"
        elif (var == var_era5_tp) or (var == var_era5_e) or (var == var_era5_pev):
            var_unit = "m"
        elif var == var_era5_sh:
            var_unit = "1"

    return var_unit


def get_rcp_desc(rcp: str):

    """
    --------------------------------------------------------------------------------------------------------------------
    Get the description of an emission scenario.

    Parameters
    ----------
    rcp : str
        Emission scenario, e.g., {cfg.rcp_ref, cfg.rcp_26, cfg.rcp_45, cfg.rcp_85}
    --------------------------------------------------------------------------------------------------------------------
    """

    rcp_desc = ""
    if rcp == rcp_ref:
        rcp_desc = "reference"
    elif ("rcp" in rcp) and (len(rcp) == 5):
        rcp_desc = rcp[0:3].upper() + " " + rcp[3] + "." + rcp[4]

    return rcp_desc


def get_d_stn(var: str):

    """
    --------------------------------------------------------------------------------------------------------------------
    Get directory of station data.

    Parameters
    ----------
    var : str
        Variable.
    --------------------------------------------------------------------------------------------------------------------
    """

    d = ""
    if var != "":
        d = d_stn + var + "/"

    return d


def get_p_stn(var: str, stn: str):

    """
    --------------------------------------------------------------------------------------------------------------------
    Get path of station data.

    Parameters
    ----------
    var : str
        Variable.
    stn : str
        Station.
    --------------------------------------------------------------------------------------------------------------------
    """

    p = d_stn + var + "/" + var + "_" + stn + ".nc"

    return p


def get_d_scen(stn: str, category: str, var: str = ""):

    """
    --------------------------------------------------------------------------------------------------------------------
    Get scenario directory.

    Parameters
    ----------
    stn : str
        Station.
    category : str
        Category.
    var : str, optional
        Variable.
    --------------------------------------------------------------------------------------------------------------------
    """

    d = d_res
    if stn != "":
        d = d + cat_stn + "/" + stn + "/"
    if category != "":
        d = d
        if (category == cat_obs) or (category == cat_raw) or (category == cat_regrid) or (category == cat_qqmap) or\
           (category == cat_qmf):
            d = d + cat_scen + "/"
        d = d + category + "/"
    if var != "":
        d = d + var + "/"

    return d


def get_d_idx(stn: str, var: str = ""):

    """
    --------------------------------------------------------------------------------------------------------------------
    Get index directory.

    Parameters
    ----------
    stn : str
        Station.
    var : str, optional
        Variable.
    --------------------------------------------------------------------------------------------------------------------
    """

    d = d_res
    if stn != "":
        d = d + cat_stn + "/" + stn + "/"
    d = d + cat_idx + "/"
    if var != "":
        d = d + var + "/"

    return d


def get_p_obs(stn_name: str, var: str, category: str = ""):

    """
    --------------------------------------------------------------------------------------------------------------------
    Get observation path (under scenario directory).

    Parameters
    ----------
    stn_name : str
        Localisation.
    var : str
        Variable.
    category : str, optional
        Category.
    --------------------------------------------------------------------------------------------------------------------
    """

    p = get_d_scen(stn_name, cat_obs) + var + "/" + var + "_" + stn_name
    if category != "":
        p = p + "_4qqmap"
    p = p + ".nc"

    return p
