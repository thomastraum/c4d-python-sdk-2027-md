<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/thinkingparticles/index.html -->

# c4d.modules.thinkingparticles <a id="c4d-modules-thinkingparticles"></a>

## *class* `c4d.modules.thinkingparticles` <a id="c4d.modules.thinkingparticles"></a>

## About TP <a id="about-tp"></a>

Thinking Particles is a rule-based particle system that offers tremendous power and flexibility, but there is no doubt that it will take some time for you to understand how to use the package.  
For any particular job there will be many different approaches and a number of solutions.  
Thinking Particles is node-based and normally uses the Cinema 4D XPresso Editor for the creation and editing of its various nodes.  
Now with the API support of Python it is possible to handle Thinking Particles in your own tag or node.  
To get the most out of Thinking Particles it is important to plan ahead, consider how all your particles are going to interact and, above all, assign different sets of particles to different particle groups.  
This way you will build in flexibility, which can save a great deal of time should you decide to change things later.  
Each particle is assigned to a particle group where you can handle a rule on.  
By default, all particles are assigned to the *All group*.  
The groups are arranged in a hierarchy that works in the same way as Cinema 4D’s XPresso manager.  
The advantage of this structure is that you can build an entire tree of groups, the top-most of which will contain all the groups belonging to that branch and thus the particles of these groups also.  
Finally, please remember to plan ahead and try things out before committing yourself to a large, complex set-up or algorithm.  
Also, keep in mind that adding shape to your particles will, naturally, slow down the viewport display speed, so it is best to experiment before adding shape to your particles.

- [`c4d.modules.thinkingparticles.TP_MasterSystem`](TP_MasterSystem/index.md#c4d.modules.thinkingparticles.TP_MasterSystem)
- [`c4d.modules.thinkingparticles.TP_PGroup`](TP_PGroup/index.md#c4d.modules.thinkingparticles.TP_PGroup)
