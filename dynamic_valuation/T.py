import numpy
from scipy.optimize import minimize_scalar


def T(v,cl=None,s_grid=[],policy=None):
  if not list(s_grid):
    s_grid=cl.s_grid
  if policy==None:
    v_new = numpy.empty_like(v)
    x_new = numpy.empty_like(v)

    for i, s in enumerate(s_grid):
        # Maximize RHS of Bellman equation at state x
        foo=minimize_scalar((lambda x: -state_action_value(cl,s_grid,s=s,v_array=v,policy=x/cl.freq)), bounds=(0, min(s,cl.policy_bound)),method='bounded')
        v_new[i]=-foo.fun
        x_new[i]=foo.x
    return v_new,x_new
  else:
    v_new = numpy.empty_like(v)

    for i, s in enumerate(s_grid):
      v_new[i] = state_action_value(cl,s_grid,s,v,policy)

    return v_new