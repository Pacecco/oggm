"""OGGM tasks.

This module is simply a shortcut to the core functions
"""
# flake8: noqa
# Entity tasks
from oggm.core.gis import define_glacier_region
from oggm.core.gis import glacier_masks
from oggm.core.gis import simple_glacier_masks
from oggm.core.gis import gridded_attributes
from oggm.core.gis import gridded_mb_attributes
from oggm.core.centerlines import compute_centerlines
from oggm.core.centerlines import compute_downstream_line
from oggm.core.centerlines import compute_downstream_bedshape
from oggm.core.centerlines import catchment_area
from oggm.core.centerlines import catchment_intersections
from oggm.core.centerlines import initialize_flowlines
from oggm.core.centerlines import catchment_width_geom
from oggm.core.centerlines import catchment_width_correction
from oggm.core.centerlines import terminus_width_correction
from oggm.core.centerlines import elevation_band_flowline
from oggm.core.centerlines import fixed_dx_elevation_band_flowline
from oggm.core.climate import glacier_mu_candidates
from oggm.core.climate import process_climate_data
from oggm.core.climate import process_custom_climate_data
from oggm.core.climate import historical_delta_method
from oggm.core.climate import historical_climate_qc
from oggm.shop.cru import process_cru_data
from oggm.shop.cru import process_dummy_cru_file
from oggm.shop.histalp import process_histalp_data
from oggm.shop.ecmwf import process_ecmwf_data
from oggm.core.gcm_climate import process_gcm_data
from oggm.core.gcm_climate import process_cesm_data
from oggm.core.gcm_climate import process_cmip5_data
from oggm.core.climate import local_t_star
from oggm.core.climate import mu_star_calibration
from oggm.core.climate import apparent_mb_from_linear_mb
from oggm.core.inversion import prepare_for_inversion
from oggm.core.inversion import mass_conservation_inversion
from oggm.core.inversion import volume_inversion
from oggm.core.inversion import filter_inversion_output
from oggm.core.inversion import distribute_thickness_per_altitude
from oggm.core.inversion import distribute_thickness_interp
from oggm.core.inversion import find_inversion_calving
from oggm.core.flowline import init_present_time_glacier
from oggm.core.flowline import run_random_climate
from oggm.core.flowline import run_from_climate_data
from oggm.core.flowline import run_constant_climate
from oggm.core.vascaling import local_t_star as vas_local_t_star
from oggm.core.vascaling import t_star_from_refmb as vas_t_star_from_refmb
from oggm.core.vascaling import find_start_area as vas_find_start_area
from oggm.core.vascaling import run_random_climate as vas_run_random_climate
from oggm.utils import copy_to_basedir

# Global tasks
from oggm.core.climate import compute_ref_t_stars
from oggm.core.vascaling import compute_ref_t_stars as vas_compute_ref_t_stars
from oggm.utils import compile_glacier_statistics
from oggm.utils import compile_run_output
from oggm.utils import compile_climate_input
from oggm.utils import compile_task_log
from oggm.utils import compile_task_time
