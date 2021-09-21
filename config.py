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

import os.path

# Constants ------------------------------------------------------------------------------------------------------------

# Reanalysis data.
obs_src_era5        = "era5"        # ERA5.
obs_src_era5_land   = "era5_land"   # ERA5-Land.
obs_src_merra2      = "merra2"      # Merra2.

# Projection data.
prj_src_cordex      = "cordex"      # CORDEX.

# Emission scenarios.
rcp_ref             = "ref"         # Reference period.
rcp_26              = "rcp26"       # Future period RCP 2.6.
rcp_45              = "rcp45"       # Future period RCP 4.5.
rcp_85              = "rcp85"       # Future period RCP 8.5.
rcp_xx              = "rcpxx"       # Any type of RCP.

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

# Units (general).
unit_deg            = "°"
unit_pct            = "%"

# Units (NetCDF).
unit_C              = "C"
unit_K              = "K"
unit_kg_m2s1        = "kg m-2 s-1"
unit_m              = "m"
unit_mm             = "mm"
unit_mm_d           = "mm d-1"
unit_m_s            = "m s-1"
unit_J_m2           = "J m-2"
unit_Pa             = "Pa"
unit_d              = "d"
unit_km_h           = "km h-1"
unit_1              = "1"

# Units (description; for plots).
unit_C_desc         = unit_deg + unit_C
unit_K_desc         = unit_K
unit_kg_m2s1_desc   = "kg/m²s)"
unit_m_desc         = unit_m
unit_mm_desc        = unit_mm
unit_mm_d_desc      = "mm/jour"
unit_m_s_desc       = "m/s"
unit_J_m2_desc      = "J/m²"
unit_Pa_desc        = unit_Pa
unit_d_desc         = "jours"
unit_km_h_desc      = "km/h"

# Dataset dimensions.
dim_lon             = "lon"
dim_lat             = "lat"
dim_rlon            = "rlon"
dim_rlat            = "rlat"
dim_longitude       = "longitude"
dim_latitude        = "latitude"
dim_time            = "time"

# ======================================================================================================================
# TODO.CUSTOMIZATION.VARIABLE.BEGIN
# Add new CORDEX AND ERA5* variables below.
# ======================================================================================================================

# Variables (cordex).
var_cordex_tas        = "tas"         # Temperature (daily mean).
var_cordex_tasmin     = "tasmin"      # Temperature (daily minimum).
var_cordex_tasmax     = "tasmax"      # Temperature (daily maximum).
var_cordex_pr         = "pr"          # Precipitation.
var_cordex_uas        = "uas"         # Wind speed, eastward.
var_cordex_vas        = "vas"         # Wind speed, northward.
var_cordex_sfcwindmax = "sfcWindmax"  # Wind speed (daily maximum).
var_cordex_ps         = "ps"          # Barometric pressure.
var_cordex_rsds       = "rsds"        # Solar radiation.
var_cordex_evspsbl    = "evspsbl"     # Evaporation.
var_cordex_evspsblpot = "evspsblpot"  # Potential evapotranspiration.
var_cordex_huss       = "huss"        # Specific humidity.
var_cordex_clt        = "clt"         # Cloud cover.

# Variables (era5 and era5_land).
var_era5_t2m        = "t2m"         # Temperature (hourly or daily mean).
var_era5_t2mmin     = "t2mmin"      # Temperature (daily minimum).
var_era5_t2mmax     = "t2mmax"      # Temperature (daily maximum).
var_era5_tp         = "tp"          # Precipitation.
var_era5_u10        = "u10"         # Wind speed, eastward (hourly or daily mean).
var_era5_u10min     = "u10min"      # Wind speed, eastward (daily minimum).
var_era5_u10max     = "u10max"      # Wind speed, eastward (daily maximum).
var_era5_v10        = "v10"         # Wind speed, northward (hourly or daily mean).
var_era5_v10min     = "v10min"      # Wind speed, northward (daily minimum).
var_era5_v10max     = "v10max"      # Wind speed, northward (daily maximum).
var_era5_uv10       = "uv10"        # Wind speed (hourly or daily mean).
var_era5_uv10min    = "uv10min"     # Wind speed (daily minimum).
var_era5_uv10max    = "uv10max"     # Wind speed (daily maximum).
var_era5_sp         = "sp"          # Barometric pressure.
var_era5_ssrd       = "ssrd"        # Solar radiation.
var_era5_e          = "e"           # Evaporation.
var_era5_pev        = "pev"         # Potential evapotranspiration.
var_era5_d2m        = "d2m"         # Dew temperature.
var_era5_sh         = "sh"          # Specific humidity.

# ======================================================================================================================
# TODO.CUSTOMIZATION.VARIABLE.END
# ======================================================================================================================

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
cat_fig_monthly     = "monthly"      # Figures (monthly).
cat_fig_daily       = "daily"        # Figures (daily).

# Calendar types.
cal_noleap          = "noleap"      # No-leap.
cal_360day          = "360_day"     # 360 days.
cal_365day          = "365_day"     # 365 days.

# Date type.
dtype_obj           = "object"
dtype_64            = "datetime64[ns]"

# Data frequency.
freq_D              = "D"           # Daily.
freq_MS             = "MS"          # Monthly.
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

# ======================================================================================================================
# TODO.CUSTOMIZATION.INDEX.BEGIN
# Add new index below.
# ======================================================================================================================

# Temperature indices --------------------------------------------------------------------------------------------------

# Extreme temperature range.
# Requirements: tasmin, tasmax
# Parameters:   [nan]
idx_etr = "etr"

# Number of days with extreme maximum temperature (> 90th percentile).
# Requirements: tasmax
# Parameters:   [nan]
idx_tx90p = "tx90p"

# Maximum heat wave length.
# Requirements: tasmin, tasmax
# Parameters:   [tasmin_thresh: float, tasmax_thresh: float, n_days: int]
#               tasmin_thresh: daily minimum temperature must be greater than a threshold value.
#               tasmax_thresh: daily maximum temperature must be greater than a threshold value.
#               n_days: minimum number of consecutive days.
idx_heat_wave_max_length = "heat_wave_max_length"

# Total heat wave length.
# Requirements: tasmin, tasmax
# Parameters:   [tasmin_thresh: float, tasmax_thresh: float, n_days: int]
#               tasmin_thresh: daily minimum temperature must be greater than a threshold value.
#               tasmax_thresh: daily maximum temperature must be greater than a threshold value.
#               n_days: Minimum number of consecutive days.
idx_heat_wave_total_length = "heat_wave_total_len"

# Number of hot spells.
# Requirements: tasmax
# Parameters:   [tasmax_thresh: float, n_days: int]
#               tasmax_thresh: daily maximum temperature must be greater than a threshold value.
#               n_days: minimum number of consecutive days.
idx_hot_spell_frequency = "hot_spell_frequency"

# Maximum hot spell length.
# Requirements: tasmax
# Parameters:   [tasmax_threshold: float, n_days: int]
#               tasmax_threshold: daily maximum temperature must be greater than this threshold.
#               n_days: minimum number of consecutive days.
idx_hot_spell_max_length = "hot_spell_max_length"

# Mean of mean temperature.
# Requirements: tasmin, tasmax
# Parameters:   [nan]
idx_tgg = "tgg"

# Mean of minimum temperature.
# Requirements: tasmin
# Parameters:   [nan]
idx_tng = "tng"

# Maximum of minimum temperature.
# Requirements: tasmin
# Parameters:   [nan]
idx_tnx = "tnx"

# Mean of maximum temperature.
# Requirements: tasmax
# Parameters:   [nan]
idx_txg = "txg"

# Maximum of maximum temperature.
# Parameters: [nan]
idx_txx = "txx"

# Number of months per year with a mean minimum temperature below a threshold.
# Requirements: tasmin
# Parameters:   [tasmin_thresh: float]
#               tasmin_thresh: daily minimum temperature must be greater than a threshold value.
idx_tng_months_below = "tng_months_below"

# Number of days per year with maximum temperature above a threshold.
# Requirements: tasmax
# Parameters:   [tasmax_thresh: float]
#               tasmax_thresh: daily maximum temperature must be greater than a threshold value.
idx_tx_days_above = "tx_days_above"

# Number of days per year with a minimum temperature below a threshold.
# Requirements: tasmin
# Parameters:   [tasmin_thresh: float, doy_min: int, doy_max: int]
#               tasmin_thresh: daily minimum temperature must be greater than a threshold value.
#               doy_min: minimum day of year to consider.
#               doy_max: maximum day of year to consider.
idx_tn_days_below = "tn_days_below"

# Number of tropical nights, i.e. with minimum temperature above a threshold.
# Requirements: tasmin
# Parameters:   [tasmin_thresh: float]
#               tasmin_thresh: daily minimum temperature must be greater than a threshold value.
idx_tropical_nights = "tropical_nights"

# Warm spell duration index.
# Requirements: tasmax
# Parameters:   [tasmax_thresh=nan, n_days: int]
#               tasmax_thresh: daily maximum temperature must be greater than a threshold value; this value is
#               calculated automatically and corresponds to the 90th percentile of tasmax values.
#               n_days: minimum number of consecutive days.
idx_wsdi = "wsdi"

# Precipitation indices ------------------------------------------------------------------------------------------------

# Largest 1-day precipitation amount.
# Requirements: pr
# Parameters:   [nan]
idx_rx1day = "rx1day"

# Largest 5-day precipitation amount.
# Requirements: pr
# Parameters:   [nan]
idx_rx5day = "rx5day"

# Maximum number of consecutive dry days.
# Requirements: pr
# Parameters:   [pr_thresh: float]
#               pr_thresh: a daily precipitation amount lower than a threshold value is considered dry.
idx_cdd = "cdd"

# Maximum number of consecutive wet days.
# Requirements: pr
# Parameters:   [pr_thresh: float]
#               pr_thresh: a daily precipitation amount greater than or equal to a threshold value is considered wet.
idx_cwd = "cwd"

# Number of dry days.
# Requirements: pr
# Parameters:   [pr_thresh: float]
#               pr_thresh: a daily precipitation amount lower than a threshold value is considered dry.
idx_dry_days = "dry_days"

# Number of wet days.
# Requirements: pr
# Parameters:   [pr_thresh: float]
#               pr_thresh: a daily precipitation amount greater than or equal to a threshold value is considered wet.
idx_wet_days = "wet_days"

# Accumulated total precipitation.
# Requirements: pr
# Parameters:   [pct=nan, doy_min: int, doy_max: int]
#               pct: the default value is nan;
#                    if a value is provided, an horizontal line is drawn on time series;
#                    if a percentile is provided (ex: 90p), the equivalent value is calculated and an horizontal line is
#                    drawn on time series.
#               doy_min: minimum day of year to consider.
#               doy_max: maximum day of year to consider.
idx_prcptot = "prcptot"

# Number of days with precipitation greater than or equal to 10 mm.
# Requirements: pr
# Parameters:   [nan]
idx_r10mm = "r10mm"

# Number of days with precipitation greater than or equal to 20 mm.
# Requirements: pr
# Parameters:   [nan]
idx_r20mm = "r20mm"

# Number of days with precipitation greater than or equal to a user-provided value.
# Requirements: pr
# Parameters:   [pr_thresh: float]
#               pr_thresh: daily precipitation amount must be greater than or equal to a threshold value.
idx_rnnmm = "rnnmm"

# Mean daily precipitation intensity.
# Requirements: pr
# Parameters:   [pr_thresh: float]
#               pr_thresh: daily precipitation amount must be greater than or equal to a threshold value.
idx_sdii = "sdii"

# Rain season.
# Requirements: pr (mandatory), evspsbl* (optional)
# Parameters:   combination of the parameters of indices idx_rain_season_start and idx_rain_season_end.
idx_rain_season = "rain_season"

# Day of year where rain season starts.
# Requirements: pr
# Parameters:   [pr_wet: float, dt_wet: int, doy_min: int, doy_max: int, pr_dry: float, dt_dry: int, dt_tot: int]
#               pr_wet: daily precipitation amount required in first 'dt_wet' days.
#               dt_wet: number of days with precipitation at season start (related to 'pr_wet').
#               doy_min: minimum day of year where season can start.
#               doy_max: minimum day of year where season can start.
#               pr_dry: daily precipitation amount under which precipitation is considered negligible.
#               dt_dry: maximum number of days in a dry period embedded into the period of 'dt_tot' days.
#               dt_tot: number of days (after the first 'dt_wet' days) after which a dry season is searched for.
idx_rain_season_start = "rain_season_start"

# Day of year where rain season ends.
# Requirements: pr (mandatory), rain_season_start_next (optional), evspsbl* (optional)
#               will search for evspsblpot, then for evspsbl
# Parameters:   [meth: str, pr: float, etp: float, dt: int, doy_min: int, doy_max: int]
#               meth: calculation method
#                   if method == "depletion": based on the period required for an amount of water to evaporate,
#                       considering that any amount of precipitation received during that period must also evaporate. If
#                       the evspsbl* dataset is not available, the daily evapotranspiration rate is assumed to be 'etp'.
#                   if method == "event": based on the occurrence (or not) of an event during the last days of a rain
#                       season. The rain season stops when no daily precipitation greater than 'pr' have occurred over a
#                       period of 'dt' days.
#                   if method == "total": based on a total amount of precipitation received during the last days of the
#                       rain season. The rain season stops when the total amount of precipitation is less than 'pr' over
#                       a period of 'dt' days.
#               pr: precipitation threshold
#                   if method == "depletion": precipitation amount that must evaporate.
#                   if method == "event": threshold daily precipitation amount during a period.
#                   if method == "total": threshold total precipitation amount over a period.
#               etp: evapotranspiration rate
#                   if method == "depletion": evapotranspiration rate.
#                   otherwise: not used.
#               dt: period length
#                   if method in ["event", "total"]: length of period (number of days) used to verify if the rain season
#                       is ending.
#                   otherwise: not used.
#               doy_min: minimum day of year where season can end.
#               doy_max: minimum day of year where season can end.
idx_rain_season_end = "rain_season_end"

# Duration of the rain season.
# Requirements: rain_season_start, rain_season_end
# Parameters:   [nan]
idx_rain_season_length = "rain_season_length"

# Quantity received during rain season.
# Requirements: pr, rain_season_start, rain_season_end
# Parameters:   [nan]
idx_rain_season_prcptot = "rain_season_prcptot"

# Total length of dry period.
# Requirements: pr
# Parameters:   [per: str, pr_tot: float, dt_dry: int, pr_dry: float, doy_min: int, doy_max: int]
#               per: period over which to combine data {"1d" = one day, "tot" = total}.
#               pr_tot: sum of daily precipitation amounts under which the period is considered dry (only if per="tot).
#               dt_dry: number of days to have a dry period.
#               pr_dry: daily precipitation amount under which precipitation is considered negligible.
#               doy_min: minimum day of year to consider.
#               doy_max: maximum day of year to consider.
idx_dry_spell_total_length = "dry_spell_total_length"

# Wind indices ---------------------------------------------------------------------------------------------------------

# Number of days per year with mean wind speed above a threshold value coming from a given direction.
# Requirements: uas, vas
# Parameters:   [speed_tresh: float, velocity_thresh_neg: float, dir_thresh: float, dir_thresh_tol: float,
#                doy_min: int, doy_max: int]
#               speed_tresh: wind speed must be greater than or equal to a threshold value.
#                    if a percentile is provided (ex: 90p), the equivalent value is calculated.
#               speed_tresh_neg: wind speed is considered negligible if smaller than or equal to a threshold value.
#               dir_thresh: wind direction (angle, in degrees) must be close to a direction given by a threshold value.
#               dir_thresh_tol: wind direction tolerance (angle, in degrees).
#               doy_min: minimum day of year to consider (nan can be provided).
#               doy_max: maximum day of year to consider (nan can be provided).
idx_wg_days_above = "wg_days_above"

# Number of days per year with maximum wind speed above a threshold value.
# Requirements: sfcWindmax
# Parameters:   [speed_tresh: float, nan, nan, nan, doy_min: int, doy_max: int]
#               speed_tresh: wind speed must be greater than or equal to a threshold value.
#                    if a percentile is provided (ex: 90p), the equivalent value is calculated.
#               doy_min: minimum day of year to consider (nan can be provided).
#               doy_max: maximum day of year to consider (nan can be provided).
idx_wx_days_above = "wx_days_above"

# Temperature-precipitation indices ------------------------------------------------------------------------------------

# Drought code.
# Requirements: tas, pr
# Parameters:   [nan]
idx_drought_code = "drought_code"

# Groups of indices ----------------------------------------------------------------------------------------------------

# Indices that are part of a group are saved in a single NetCDF file.
idx_groups = [[idx_rain_season, [idx_rain_season_start, idx_rain_season_end, idx_rain_season_length,
                                 idx_rain_season_prcptot]]]

# ==========================================================
# TODO.CUSTOMIZATION.INDEX.END
# ==========================================================

# Statistics.
stat_mean           = "mean"        # Mean value.
stat_min            = "min"         # Minimum value.
stat_max            = "max"         # Maximum value.
stat_sum            = "sum"         # Sum of values.
stat_quantile       = "quantile"    # Value associated with a given quantile.

# Conversion coefficients.
spd                 = 86400         # Number of seconds per day.
d_KC                = 273.15        # Temperature difference between Kelvin and Celcius.
km_h_per_m_s        = 3.6           # Number of km/h per m/s.

# Files.
f_sep               = ","           # File separator (only in CSV files containing observations).
f_csv               = "csv"         # CSV file type (comma-separated values).
f_png               = "png"         # PNG file type (image).
f_tif               = "tif"         # TIF file type (image, potentially georeferenced).
f_nc                = "nc"          # NetCDF file type.
f_nc4               = "nc4"         # NetCDF v4 file type.
f_ext_csv           = "." + f_csv   # CSV file extension.
f_ext_png           = "." + f_png   # PNG file extension.
f_ext_tif           = "." + f_tif   # TIF file extension.
f_ext_nc            = "." + f_nc    # NetCDF file extension.
f_ext_nc4           = "." + f_nc4   # NetCDF v4 file extension.
f_ext_log           = ".log"        # LOG file extension.

# Context --------------------------------------------------------------------------------------------------------------

# Country and project.
country             = ""            # Country name.
project             = ""            # Project acronym.

# Emission scenarios, periods and horizons.
rcps                = [rcp_26, rcp_45, rcp_85]                                  # All emission scenarios.
per_ref             = [1981, 2010]                                              # Reference period.
per_fut             = [1981, 2100]                                              # Future period.
per_hors            = [[1981, 2010], [2021, 2040], [2041, 2060], [2061, 2080]]  # Horizons.

# Boundary box.
lon_bnds            = [0, 0]        # Longitude boundaries.
lat_bnds            = [0, 0]        # Latitude boundaries.
ctrl_pt             = None          # Control point: [longitude, latitude] (this is for statistics.

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
# The parameter 'd_bounds' is only used to compute statistics; this includes .csv files in the 'stat' directory and
# time series (.png and .csv)). The idea behind this is to export heat maps (.png and .csv) that covers values included
# in the box defined by 'lon_bnds' and 'lat_bnds'.
d_proj              = ""            # Projections.
d_ra_raw            = ""            # Reanalysis set (default frequency, usually hourly).
d_bounds            = ""            # geog.json file comprising political boundaries.
region              = ""            # Region name or acronym.
# Output-only files and directories.
d_stn               = ""            # Observations or reanalysis.
d_res               = ""            # Results.
# Input and output files and directories.
d_exec              = ""            # Base directory #3 (stations and output).
d_ra_day            = ""            # Reanalysis set (aggregated frequency, i.e. daily).

# File option.
opt_force_overwrite = False         # If True, all NetCDF files and calibration diagrams will be overwritten.

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
opt_calib_perturb   = []            # Perturbation: list of [variable,value]. "*" applies to all variables.
opt_calib_quantiles  = [1.00, 0.99, 0.90, 0.50, 0.10, 0.01, 0.00]  # Quantiles.

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
idx_codes           = []            # Index codes.
idx_names           = []            # Index names.
idx_params          = []            # Index parameters.

# Step 7 - Statistics --------------------------------------------------------------------------------------------------

opt_stat            = [True, True]    # If True, calculate statistics [for scenarios, for indices].
opt_stat_quantiles  = [1.00, 0.90, 0.50, 0.10, 0.00]  # Quantiles.
opt_stat_clip       = False           # If True, clip according to 'd_bounds'.
opt_save_csv        = [False, False]  # If True, save results to CSV files [for scenarios, for indices].

# Step 8 - Visualization -----------------------------------------------------------------------------------------------

# Plots.
opt_plot              = [True, True]    # If True, actives plot generation [for scenarios, for indices].
opt_map               = [False, False]  # If True, generate heat maps [for scenarios, for indices].
opt_map_delta         = [False, False]  # If True, generate delta heat maps [for scenarios, for indices].
opt_map_clip          = False           # If True, clip according to 'd_bounds'.
opt_map_quantiles     = []              # Quantiles for which a map is required.
opt_map_formats       = [f_png]         # Map formats.
opt_map_spat_ref      = ""              # Spatial reference (starts with: EPSG).
opt_map_res           = -1              # Map resolution.
opt_map_discrete      = False           # If true, discrete color scale in maps (rather than continuous).

# Color associated with specific datasets (calibration plots).
col_sim_adj_ref     = "blue"            # Simulation (bias-adjusted) for the reference period.
col_sim_ref         = "orange"          # Simulation (non-adjusted) for the reference period
col_obs             = "green"           # Observations.
col_sim_adj         = "red"             # Simulation (bias-adjusted).
col_sim_fut         = "purple"          # Simulation (non-adjusted) for the future period.

# Colors for reference dataset and RCPs.
col_ref             = "black"           # Reference period.
col_rcp26           = "blue"            # RCP 2.6.
col_rcp45           = "green"           # RCP 4.5.
col_rcp85           = "red"             # RCP 8.5.

# Colors for plots.
# The first color is for low values, and the second color is for high values.
opt_plot_col_2cla_temp = ["cornflowerblue", "indianred"]  # Temperature variables.
opt_plot_col_2cla_prec = ["darkgoldenrod", "g"]           # Precipitation variables.
opt_plot_col_2cla_wind = ["mediumpurple", "orange"]       # Wind variables.

# Color maps apply to categories of variables and indices.
# +----------------------------+------------+------------+
# | Variable, category         |   Variable |      Index |
# +----------------------------+------------+------------+
# | temperature, high values   | temp_var_1 | temp_idx_1 |
# | temperature, low values    |          - | temp_idx_2 |
# | precipitation, high values | prec_var_1 | prec_idx_1 |
# | precipitation, low values  |          - | prec_idx_2 |
# | precipitation, dates       |          - | prec_idx_3 |
# | wind                       | wind_var_1 | wind_idx_1 |
# +----------------------------+------------+------------+
# The 1st scheme is for absolute values.
# The 2nd scheme is divergent and his made to represent delta values when both negative and positive values are present.
# It combines the 3rd and 4th schemes.
# The 3rd scheme is for negative-only delta values.
# The 4th scheme is for positive-only delta values.
opt_map_col_temp_var   = ["viridis", "RdBu_r", "Blues_r", "Reds"]       # Temperature variables.
opt_map_col_temp_idx_1 = opt_map_col_temp_var                           # Temperature indices (high).
opt_map_col_temp_idx_2 = ["plasma_r", "RdBu", "Reds_r", "Blues"]        # Temperature indices (low).
opt_map_col_prec_var   = ["Blues", "BrWhGr", "Browns_r", "Greens"]      # Precipitation variables.
opt_map_col_prec_idx_1 = opt_map_col_prec_var                           # Precipitation indices (high).
opt_map_col_prec_idx_2 = ["Oranges", "BrWhGr_r", "Greens_r", "Browns"]  # Precipitation indices (low).
opt_map_col_prec_idx_3 = ["viridis", "RdBu_r", "Blues_r", "Reds"]       # Precipitation indices (other).
opt_map_col_wind_var   = ["None", "RdBu_r", "Blues_r", "Reds"]          # Wind variables.
opt_map_col_wind_idx_1 = ["Reds", "RdBu_r", "Blues_r", "Reds"]          # Wind indices.
opt_map_col_default    = ["viridis", "RdBu_r", "Blues_r", "Reds"]       # Other variables and indices.


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


def extract_idx(idx_code: str) -> str:

    """
    --------------------------------------------------------------------------------------------------------------------
    Extract index name.

    Parameters:
    idx_code : str
        Index code.
    --------------------------------------------------------------------------------------------------------------------
    """

    pos = idx_code.rfind("_")
    if pos >= 0:
        tokens = idx_code.split("_")
        if tokens[len(tokens) - 1].isdigit():
            return idx_code[0:pos]

    return idx_code


def get_desc(varidx_code: str, set_name: str = "cordex"):

    """
    --------------------------------------------------------------------------------------------------------------------
    Gets the description of an index.

    Parameters
    ----------
    varidx_code : str
        Climate variable or index code.
    set_name : str
        Station name.
    --------------------------------------------------------------------------------------------------------------------
    """

    desc = ""

    varidx_name = varidx_code if varidx_code in variables_cordex else extract_idx(varidx_code)

    # CORDEX.
    if varidx_name in variables_cordex:

        if varidx_name in [var_cordex_tas, var_cordex_tasmin, var_cordex_tasmax]:
            desc = "Température"
        elif varidx_name == var_cordex_ps:
            desc = "Pression barométrique"
        elif varidx_name == var_cordex_pr:
            desc = "Précipitation"
        elif varidx_name == var_cordex_evspsbl:
            desc = "Évaporation"
        elif varidx_name == var_cordex_evspsblpot:
            desc = "Évapotransp. pot."
        elif varidx_name == var_cordex_rsds:
            desc = "Radiation solaire"
        elif varidx_name in [var_cordex_uas, var_cordex_vas, var_cordex_sfcwindmax]:
            desc = "Vent"
            if varidx_name == var_cordex_uas:
                desc += " (dir. est)"
            elif varidx_name == var_cordex_vas:
                desc += " (dir. nord)"
        elif varidx_name == var_cordex_clt:
            desc = "Couvert nuageux"
        elif varidx_name == var_cordex_huss:
            desc = "Humidité spécifique"

    # ERA5 and ERA5-Land.
    elif (set_name == obs_src_era5) or (set_name == obs_src_era5_land):
        if varidx_name == var_era5_d2m:
            desc = "Point de rosée"
        elif varidx_name == var_era5_t2m:
            desc = "Température"
        elif varidx_name == var_era5_sp:
            desc = "Pression barométrique"
        elif varidx_name == var_era5_tp:
            desc = "Précipitation"
        elif varidx_name == var_era5_u10:
            desc = "Vent (dir. est)"
        elif varidx_name == var_era5_v10:
            desc = "Vent (dir. nord)"
        elif varidx_name == var_era5_ssrd:
            desc = "Radiation solaire"
        elif varidx_name == var_era5_e:
            desc = "Évaporation"
        elif varidx_name == var_era5_pev:
            desc = "Évapotransp. pot."
        elif varidx_name == var_era5_sh:
            desc = "Humidité spécifique"

    # Index.
    else:

        # Extract thresholds.
        idx_params_loc = idx_params[idx_codes.index(varidx_code)]

        # ==================================================================================================================
        # TODO.CUSTOMIZATION.INDEX.BEGIN
        # ==================================================================================================================

        # Temperature.
        if varidx_name in [idx_tx_days_above, idx_tx90p, idx_tn_days_below]:
            if varidx_name in [idx_tx_days_above, idx_tx90p]:
                desc = "Nbr jours chauds (Tmax>" + str(idx_params_loc[0]) + get_unit(var_cordex_tasmax)
            else:
                desc = "Nbr jours frais (Tmin<" + str(idx_params_loc[0]) + get_unit(var_cordex_tasmin)
            if len(idx_params_loc) == 3:
                desc += "; jours " + str(idx_params_loc[1]) + "-" + str(idx_params_loc[2])
            desc += ")"
        elif varidx_name == idx_tropical_nights:
            desc = "Nbr nuits chaudes (Tmin>" + str(idx_params_loc[0]) + get_unit(var_cordex_tasmin) + ")"
        elif varidx_name == idx_tng_months_below:
            desc = "Nbr mois frais (μ(Tmin,mois)<" + str(idx_params_loc[0]) + get_unit(var_cordex_tasmin) + ")"

        elif varidx_name in [idx_hot_spell_frequency, idx_hot_spell_max_length, idx_heat_wave_max_length,
                             idx_heat_wave_total_length, idx_wsdi]:
            if varidx_name == idx_hot_spell_frequency:
                desc = "Nbr pér chaudes"
            elif varidx_name == idx_hot_spell_max_length:
                desc = "Durée max pér chaudes"
            elif varidx_name == idx_heat_wave_max_length:
                desc = "Durée max vagues chaleur"
            elif varidx_name == idx_heat_wave_total_length:
                desc = "Durée tot vagues chaleur"
            elif varidx_name == idx_wsdi:
                desc = "Indice durée pér chaudes"
            if varidx_name in [idx_hot_spell_frequency, idx_hot_spell_max_length, idx_wsdi]:
                desc += " (Tmax≥" + str(idx_params_loc[0]) + get_unit(var_cordex_tasmax) + ", " +\
                    str(idx_params_loc[1]) + "j)"
            else:
                desc += " (" +\
                    "Tmin≥" + str(idx_params_loc[0]) + get_unit(var_cordex_tasmin) + ", " + \
                    "Tmax≥" + str(idx_params_loc[1]) + get_unit(var_cordex_tasmax) + ", " + \
                    str(idx_params_loc[2]) + "j)"

        elif varidx_name == idx_tgg:
            desc = "Moyenne de (Tmin+Tmax)/2"

        elif varidx_name == idx_tng:
            desc = "Moyenne de Tmin"

        elif varidx_name == idx_tnx:
            desc = "Maximum de Tmin"

        elif varidx_name == idx_txg:
            desc = "Moyenne de Tmax"

        elif varidx_name == idx_txx:
            desc = "Maximum de Tmax"

        elif varidx_name == idx_etr:
            desc = "Écart extreme (Tmax-Tmin)"

        # Precipitation.
        elif varidx_name in [idx_rx1day, idx_rx5day, idx_prcptot, idx_rain_season_prcptot]:
            desc =\
                "Cumul P " + ("(1j" if varidx_name == idx_rx1day else "(5j" if varidx_name == idx_rx5day else "(total")
            if (varidx_name == idx_prcptot) and (len(idx_params_loc) == 3):
                desc += "; jours " + str(idx_params_loc[1]) + "-" + str(idx_params_loc[2])
            desc += ")"

        elif varidx_name in [idx_cwd, idx_cdd, idx_r10mm, idx_r20mm, idx_rnnmm, idx_wet_days, idx_dry_days]:
            desc = "Nbr jours"
            if varidx_name == idx_cwd:
                desc += " consécutifs"
            desc += " où P" + ("<" if varidx_name in [idx_cdd, idx_dry_days] else "≥") +\
                    str(idx_params_loc[0]) + get_unit(var_cordex_pr)

        elif varidx_name == idx_sdii:
            desc = "Intensité moyenne P"

        if varidx_name == idx_rain_season_start:
            desc = "Début saison pluie (ΣP≥" + str(idx_params_loc[0]) + unit_mm + " en " + \
                       str(idx_params_loc[1]) + "j; sans P<" + str(idx_params_loc[4]) + "mm/j * " + \
                       str(idx_params_loc[5]) + "j sur " + str(idx_params_loc[6]) + "j)"

        elif varidx_name == idx_rain_season_end:
            if idx_params_loc[0] == "depletion":
                desc = "Fin saison pluie (Σ(P-ETP)<" + str(idx_params_loc[1]) + unit_mm + " en ≥" +\
                       str(idx_params_loc[1]) + "/" + str(idx_params_loc[2]) + "j)"
            else:
                desc = "Fin saison pluie (P<" + str(idx_params_loc[1]) + unit_mm + "/j pendant " +\
                       str(idx_params_loc[3]) + "j)"

        elif varidx_name == idx_rain_season_length:
            desc = "Durée saison pluie"

        elif varidx_name == idx_dry_spell_total_length:
            desc = "Durée totale périodes sèches (P<" + str(idx_params_loc[0]) + "mm/j * " +\
                       str(idx_params_loc[1]) + "j"
            if (idx_params_loc[2] == "day") and (str(idx_params_loc[3]) != "nan") and (str(idx_params_loc[4]) != "nan"):
                desc += "; jours " + str(idx_params_loc[3]) + "-"  + str(idx_params_loc[4])
            desc += ")"

        # Temperature-precipitation.
        elif varidx_name == idx_drought_code:
            desc = "Code sécheresse"

        # Wind.
        elif varidx_name in [idx_wg_days_above, idx_wx_days_above]:
            desc = "Durée totale vent fort (V" + ("moy" if varidx_name == idx_wg_days_above else "max") + "≥" +\
                       str(idx_params_loc[0]) + unit_km_h
            if str(idx_params_loc[2]) != "nan":
                desc += "; " + str(idx_params_loc[2]) + "±" + str(idx_params_loc[3]) + "º"
            if (varidx_name == idx_wg_days_above) and (len(idx_params_loc) == 6):
                desc += "; jours " + str(idx_params_loc[4]) + " à " + str(idx_params_loc[5])
            desc += ")"

        # ==============================================================================================================
        # TODO.CUSTOMIZATION.INDEX.END
        # ==============================================================================================================

    return desc


def get_plot_title(stn: str, varidx_code: str, rcp: str = None, per: [int] = None, stat: str = None, q: float = None):

    """
    --------------------------------------------------------------------------------------------------------------------
    Get plot title.

    Parameters
    ----------
    stn : str
        Station name.
    varidx_code : str
        Climate variable or index code.
    rcp: str, Optional
        RCP emission scenario.
    per: [int, int], Optional
        Period of interest, for instance, [1981, 2010].
    stat: str, Optional
        Statistic = {"mean", "min", "max", "quantile"}
    q: float, Optional
        Quantile.
    --------------------------------------------------------------------------------------------------------------------
    """

    varidx_name = varidx_code if varidx_code in variables_cordex else extract_idx(varidx_code)

    # Format items.
    stn_str = (str.upper(stn).replace("_", "") if opt_ra else stn.capitalize())
    rcp_str = ("" if rcp is None else
               ", " + ("référence" if rcp == rcp_ref else str.upper(rcp)[0:3] + rcp[3] + "." + rcp[4]))
    per_str = ("" if per is None else ", " + str(per[0]) + "-" + str(per[1]))
    stat_str = ""
    if stat is not None:
        if stat == stat_mean:
            stat_str = ", moyenne"
        elif stat in [stat_min, stat_max]:
            stat_str = ", " + stat
        else:
            stat_str = ", q" + str(int(q * 100)).rjust(2, "0")

    title = varidx_name + "\n" + stn_str + rcp_str + per_str + stat_str

    return title


def get_plot_ylabel(varidx_name: str):

    """
    --------------------------------------------------------------------------------------------------------------------
    Get plot y-label.

    Parameters
    ----------
    varidx_name : str
        Climate variable or index name.
    --------------------------------------------------------------------------------------------------------------------
    """

    if varidx_name in variables_cordex:

        ylabel = get_desc(varidx_name) + " (" + get_unit(varidx_name) + ")"

    else:

        # ==============================================================================================================
        # TODO.CUSTOMIZATION.INDEX.BEGIN
        # ==============================================================================================================

        ylabel = ""

        # Temperature.
        if varidx_name in [idx_tx_days_above, idx_tn_days_below, idx_tng_months_below, idx_hot_spell_frequency,
                           idx_hot_spell_max_length, idx_heat_wave_max_length, idx_heat_wave_total_length,
                           idx_tropical_nights, idx_tx90p]:
            ylabel = "Nbr"
            if varidx_name == idx_tng_months_below:
                ylabel += " mois"
            elif varidx_name != idx_hot_spell_frequency:
                ylabel += " jours"

        elif varidx_name in [idx_txx, idx_txg]:
            ylabel = get_desc(var_cordex_tasmax) + " (" + get_unit(var_cordex_tasmax) + ")"

        elif varidx_name in [idx_tnx, idx_tng]:
            ylabel = get_desc(var_cordex_tasmin) + " (" + get_unit(var_cordex_tasmin) + ")"

        elif varidx_name == idx_tgg:
            ylabel = get_desc(var_cordex_tas) + " (" + get_unit(var_cordex_tas) + ")"

        elif varidx_name == idx_etr:
            ylabel = "Écart de température (" + get_unit(var_cordex_tas) + ")"

        elif varidx_name == idx_wsdi:
            ylabel = "Indice"

        elif varidx_name == idx_drought_code:
            ylabel = "Code"

        # Precipitation.
        elif varidx_name in [idx_cwd, idx_cdd, idx_r10mm, idx_r20mm, idx_rnnmm, idx_wet_days, idx_dry_days,
                             idx_rain_season_length]:
            ylabel = "Nbr jours"

        elif varidx_name in [idx_rx1day, idx_rx5day, idx_prcptot, idx_rain_season_prcptot, idx_sdii]:
            ylabel = get_desc(var_cordex_pr) + " (" + get_unit(var_cordex_pr)
            if varidx_name == idx_sdii:
                ylabel += "/day"
            ylabel += ")"

        elif varidx_name in [idx_rain_season_start, idx_rain_season_end]:
            ylabel = "Jour de l'année"

        elif varidx_name in [idx_wg_days_above, idx_wx_days_above, idx_dry_spell_total_length]:
            ylabel += "Nbr jours"

        # ==============================================================================================================
        # TODO.CUSTOMIZATION.INDEX.END
        # ==============================================================================================================

    return ylabel


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
             [var_cordex_sfcwindmax, var_era5_uv10max], [var_cordex_ps, var_era5_sp], [var_cordex_rsds, var_era5_ssrd],
             [var_cordex_evspsbl, var_era5_e], [var_cordex_evspsblpot, var_era5_pev], [var_cordex_huss, var_era5_sh]]

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


def get_unit(varidx_name: str, set_name: str = prj_src_cordex):

    """
    --------------------------------------------------------------------------------------------------------------------
    Gets the unit of a variable.

    Parameters
    ----------
    varidx_name : str
        Climate or variable or index name.
    set_name : str
        Station name.
    --------------------------------------------------------------------------------------------------------------------
    """

    unit = ""

    if varidx_name in variables_cordex:
        if (varidx_name == var_cordex_tas) or (varidx_name == var_cordex_tasmin) or (varidx_name == var_cordex_tasmax):
            unit = unit_C_desc
        elif varidx_name == var_cordex_rsds:
            unit = unit_Pa_desc
        elif varidx_name in [var_cordex_pr, var_cordex_evspsbl, var_cordex_evspsblpot]:
            unit = unit_mm_desc
        elif (varidx_name == var_cordex_uas) or\
             (varidx_name == var_cordex_vas) or\
             (varidx_name == var_cordex_sfcwindmax):
            unit = unit_km_h_desc
        elif varidx_name == var_cordex_clt:
            unit = unit_pct
        elif varidx_name == var_cordex_huss:
            unit = unit_1

    elif (set_name == obs_src_era5) or (set_name == obs_src_era5_land):
        if (varidx_name == var_era5_d2m) or (varidx_name == var_era5_t2m):
            unit = unit_deg
        elif varidx_name == var_era5_sp:
            unit = unit_Pa
        elif (varidx_name == var_era5_u10) or (varidx_name == var_era5_u10min) or (varidx_name == var_era5_u10max) or\
             (varidx_name == var_era5_v10) or (varidx_name == var_era5_v10min) or (varidx_name == var_era5_v10max):
            unit = unit_m_s
        elif varidx_name == var_era5_ssrd:
            unit = unit_J_m2
        elif (varidx_name == var_era5_tp) or (varidx_name == var_era5_e) or (varidx_name == var_era5_pev):
            unit = unit_m
        elif varidx_name == var_era5_sh:
            unit = unit_1

    else:

        # ==============================================================================================================
        # TODO.CUSTOMIZATION.INDEX.BEGIN
        # ==============================================================================================================

        if varidx_name in [idx_tx_days_above, idx_tn_days_below, idx_tx90p, idx_tropical_nights, idx_tng_months_below,
                           idx_hot_spell_frequency, idx_wsdi, idx_cwd, idx_cdd, idx_r10mm, idx_r20mm, idx_rnnmm,
                           idx_wet_days, idx_dry_days, idx_rain_season_start, idx_rain_season_end, idx_drought_code,
                           idx_wg_days_above, idx_wx_days_above]:
            unit = unit_1
        elif varidx_name in [idx_hot_spell_max_length, idx_heat_wave_max_length, idx_heat_wave_total_length]:
            unit = unit_d
        elif varidx_name in [idx_tgg, idx_tng, idx_tnx, idx_txg, idx_txx, idx_etr, idx_rain_season_length,
                             idx_dry_spell_total_length]:
            unit = unit_C
        elif varidx_name in [idx_rx1day, idx_rx5day, idx_prcptot, idx_rain_season_prcptot]:
            unit = unit_mm
        elif varidx_name in [idx_sdii]:
            unit = unit_mm_d

        # ==============================================================================================================
        # TODO.CUSTOMIZATION.INDEX.END
        # ==============================================================================================================

    return unit


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

    p = d_stn + var + "/" + var + "_" + stn + f_ext_nc

    return p


def get_d_scen(stn: str, cat: str, var: str = ""):

    """
    --------------------------------------------------------------------------------------------------------------------
    Get scenario directory.

    Parameters
    ----------
    stn : str
        Station.
    cat : str
        Category.
    var : str, optional
        Variable.
    --------------------------------------------------------------------------------------------------------------------
    """

    d = d_res
    if stn != "":
        d = d + cat_stn + "/" + stn + ("_" + region if region != "" else "") + "/"
    if cat != "":
        d = d
        if (cat == cat_obs) or (cat == cat_raw) or (cat == cat_regrid) or (cat == cat_qqmap) or (cat == cat_qmf):
            d = d + cat_scen + "/"
        d = d + cat + "/"
    if var != "":
        d = d + var + "/"

    return d


def get_d_idx(stn: str, idx_name: str = ""):

    """
    --------------------------------------------------------------------------------------------------------------------
    Get index directory.

    Parameters
    ----------
    stn : str
        Station.
    idx_name : str, optional
        Index name.
    --------------------------------------------------------------------------------------------------------------------
    """

    d = d_res
    if stn != "":
        d = d + cat_stn + "/" + stn + ("_" + region if region != "" else "") + "/"
    d = d + cat_idx + "/"
    if idx_name != "":
        d = d + idx_name + "/"

    return d


def get_idx_group(idx_item: str = ""):

    """
    --------------------------------------------------------------------------------------------------------------------
    Get index directory.

    Parameters
    ----------
    idx_item : str, optional
        Index name.
    --------------------------------------------------------------------------------------------------------------------
    """

    idx_group = idx_item

    for i in range(len(idx_groups)):

        if idx_item in idx_groups[i][1]:
            idx_group = idx_groups[i][0] + idx_item.replace(idx_item, "")
            break

    return idx_group


def get_p_obs(stn_name: str, var: str, cat: str = ""):

    """
    --------------------------------------------------------------------------------------------------------------------
    Get observation path (under scenario directory).

    Parameters
    ----------
    stn_name : str
        Localisation.
    var : str
        Variable.
    cat : str, optional
        Category.
    --------------------------------------------------------------------------------------------------------------------
    """

    p = get_d_scen(stn_name, cat_obs) + var + "/" + var + "_" + stn_name
    if cat != "":
        p = p + "_4qqmap"
    p = p + f_ext_nc

    return p


def explode_idx_l(idx_group_l) -> [str]:

    """
    --------------------------------------------------------------------------------------------------------------------
    Explode a list of index names or codes, e.g. [rain_season_1, rain_season_2] into
    [rain_season_start_1, rain_season_end_1, rain_season_length_1, rain_season_prcptot_1,
     rain_season_start_2, rain_season_end_2, rain_season_length_2, rain_season_prcptot_2].

    Parameters
    ----------
    idx_group_l : [str]
        List of climate index groups.
    --------------------------------------------------------------------------------------------------------------------
    """

    idx_l_new = []

    # Loop through index names or codes.
    for i in range(len(idx_group_l)):
        idx_code = idx_group_l[i]

        # Loop through index groups.
        in_group = False
        for j in range(len(idx_groups)):

            # Explode and add to list.
            if idx_groups[j][0] in idx_code:
                in_group = True

                # Extract instance number of index (ex: "_1").
                no = idx_code.replace(idx_code, "")

                # Loop through embedded indices.
                for k in range(len(idx_groups[j][1])):
                    idx_l_new.append(idx_groups[j][1][k] + no)

        if not in_group:
            idx_l_new.append(idx_code)

    return idx_l_new


# def sel_idx_group(idx_item: str):
#
#    """
#    --------------------------------------------------------------------------------------------------------------------
#    Select the name of each group that includes a given index.
#
#    Parameters
#    ----------
#    idx_item : str
#        Index name or code.
#    --------------------------------------------------------------------------------------------------------------------
#    """
#
#    # Loop through index groups.
#    for i in range(len(idx_groups)):
#
#        if idx_item in idx_groups[i][1]:
#            return idx_groups[i][0]
#
#   return None


# def sel_idx_groups(idx_items: [str]) -> [str]:
#
#    """
#    --------------------------------------------------------------------------------------------------------------------
#    Select the name of each group that includes a given index.
#
#    Parameters
#    ----------
#    idx_items : [str]
#        Index names or codes.
#    --------------------------------------------------------------------------------------------------------------------
#    """
#
#    idx_groups_l = []
#
#    # Loop through indices.
#    for i in range(len(idx_items)):
#
#        idx_group_i = sel_idx_group(idx_items[i])
#
#        if idx_group_i is not None:
#            idx_groups_l.append(idx_group_i)
#
#    return list(set(idx_groups_l))


def get_equivalent_idx_path(p: str, varidx_code_a: str, varidx_code_b: str, stn: str, rcp: str) -> str:

    """
    --------------------------------------------------------------------------------------------------------------------
    Determine the equivalent path for another variable or index.

    Parameters
    ----------
    p : str
        Path associated with 'varidx_code_a'.
    varidx_code_a : str
        Climate variable or index to be replaced.
    varidx_code_b : str
        Climate variable or index to replace with.
    stn : str
        Station name.
    rcp : str
        Emission scenario.
    --------------------------------------------------------------------------------------------------------------------
    """

    # Determine if we have variables or indices.
    a_is_var = extract_idx(varidx_code_a) in variables_cordex
    b_is_var = extract_idx(varidx_code_b) in variables_cordex
    fn = os.path.basename(p)

    # No conversion required.
    if varidx_code_a != varidx_code_b:

        # Variable->Variable or Index->Index.
        if (a_is_var and b_is_var) or (not a_is_var and not b_is_var):
            p = p.replace(extract_idx(varidx_code_a), extract_idx(varidx_code_b))

        # Variable->Index (or the opposite)
        else:
            # Variable->Index.
            if a_is_var and not b_is_var:
                p = get_d_idx(stn, varidx_code_b)
            # Index->Variable.
            else:
                if rcp == rcp_ref:
                    p = get_d_stn(varidx_code_b)
                else:
                    p = get_d_scen(stn, cat_qqmap, varidx_code_b)
            # Both.
            if rcp == rcp_ref:
                p += extract_idx(varidx_code_b) + "_" + rcp_ref + f_ext_nc
            else:
                p += fn.replace(extract_idx(varidx_code_a) + "_", extract_idx(varidx_code_b) + "_")

    return p
