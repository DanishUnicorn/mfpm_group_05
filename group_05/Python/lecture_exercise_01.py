# A glass of whole unhomogenised milk has been left on the table.
"""
# 1) Calculate how long it takes for the milk fat globules to rise to the top, assuming the following parameters:
"""
fat_globule_dia = 6.0*10**-6 # fat globule diameter in meters
rho_milk_fat = 911.0 # density of milk fat in g/L
rho_skim_milk = 1036.0 # density of skim milk in g/L 
mu_skim_milk = 1.5*10**-3 # viscosity of skim milk in Pa·s (Remember to convert from mPa·s to Pa·s!)
h_glass = 15.0 # height of the glass in cm 
g = 9.81 # acceleration due to gravity in m/s^2

# We can calculate the particle velocity using the Stoke's law: v_P=(a*d^2*(Delta_rho)*g)/(18*mu_c) where:
# v_P is the particle velocity
# a is the acceleration due to gravity
# d is the diameter of the particle
# Delta_rho is the difference in density between the particle and the fluid
# mu_c is the viscosity of the fluid

# We can calculate the time it takes for the particle to rise to the top of the glass using the equation: t=h/v_P where:
# t is the time taken for the particle to rise to the top of the glass
# h is the height of the glass
# v_P is the particle velocity

# Calculate the difference in density between the fat globule and the skim milk
Delta_rho = rho_skim_milk - rho_milk_fat

# Calculate the particle velocity
v_P = (g*(fat_globule_dia**2)*Delta_rho)/(18*mu_skim_milk)

# Calculate the time taken for the fat globule to rise to the top of the glass
t = (h_glass/100)/v_P # Convert height of the glass from cm to m
t_min = t/60
t_hour = t_min/60
t_day = t_hour/24

# Print the time taken for the fat globule to rise to the top of the glass
print(f"The velocity of the fat globule is {v_P:.10f} m/s.")
print(f"Time taken for the fat globule to rise to the top of the glass: {t:.2f} s ({t_min:.2f} min, {t_hour:.2f} h, {t_day:.2f} days)")
"""
# 2) How long is the creaming time if the glass is left in the fridge and cold agglutination has caused the formation of fat globule clusters with an average diameter of 60 μm? All other parameters remain unaffected:
"""
fat_globule_dia_2 = 60.0*10**-6 # fat globule diameter in meters

# We can calculate the particle velocity using the Stoke's law: v_P=(a*d^2*(Delta_rho)*g)/(18*mu_c) where:
# v_P is the particle velocity
# a is the acceleration due to gravity
# d is the diameter of the particle
# Delta_rho is the difference in density between the particle and the fluid
# mu_c is the viscosity of the fluid

# We can calculate the time it takes for the particle to rise to the top of the glass using the equation: t=h/v_P where:
# t is the time taken for the particle to rise to the top of the glass
# h is the height of the glass
# v_P is the particle velocity

# Calculate the difference in density between the fat globule and the skim milk
Delta_rho = rho_skim_milk - rho_milk_fat

# Calculate the particle velocity
v_P_2 = (g*(fat_globule_dia_2**2)*Delta_rho)/(18*mu_skim_milk)

# Calculate the time taken for the fat globule to rise to the top of the glass
t_2 = (h_glass/100)/v_P_2 # Convert height of the glass from cm to m
t_min_2 = t_2/60
t_hour_2 = t_min_2/60
t_day_2 = t_hour_2/24

# Print the time taken for the fat globule to rise to the top of the glass
print(f"The velocity of the big fat globule is {v_P_2:.10f} m/s.")
print(f"Time taken for the big fat globule to rise to the top of the glass: {t_2:.2f} s ({t_min_2:.2f} min, {t_hour_2:.2f} h, {t_day_2:.2f} days)")