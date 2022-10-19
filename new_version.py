#%%
import numpy as np 
from astropy.cosmology import Planck18 as cosmo

def mpc_to_gly(dist):
    return dist*0.0032637977445371

z = 1

age_now = cosmo.age(0).value
age_at_z = cosmo.age(z).value
ligh_travel_time = cosmo.lookback_time(z).value
como_dist_mpc = cosmo.comoving_distance(z).value
como_dist_gly = mpc_to_gly(como_dist_mpc)
como_volume = cosmo.comoving_volume(z).value*(0.001**3)
angular_diameter_mpc = cosmo.angular_diameter_distance(z).value
angular_diameter_gly = mpc_to_gly(angular_diameter_mpc)
angular_scale = cosmo.kpc_proper_per_arcmin(z).value/60
lum_dist = cosmo.luminosity_distance(z).value

omega_vac = 1-cosmo.Om0

print('For H_0 = {}, Omega_M = {}, Omega_Vac = {} and z = {}'. format(cosmo.H0.value, cosmo.Om0, omega_vac, z))
# %%
