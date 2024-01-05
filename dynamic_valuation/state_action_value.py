from scipy.interpolate import interp1d as interp

def state_action_value(cl,s_grid,s, v_array,policy):

    v = interp(s_grid, v_array)
    sav=lambda x: cl.W(s,x)+ cl.β * v(max(cl.s_min,s+cl.sdot(s,x)))

    if callable(policy):
      return sav(policy(s))
    else:
      return sav(policy)