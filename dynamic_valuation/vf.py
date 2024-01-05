def vf(cl,s):
      if abs(s-cl.eq)<cl.ds:
        return cl.veq
      else:
        return  cl.W(s,cl.x(s))+cl.β*vf(cl,s+cl.sdot(s,cl.x(s)))