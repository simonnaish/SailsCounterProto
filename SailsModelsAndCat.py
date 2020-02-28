
""""bl=blp='blade'
s1=s1p='s1'
gt=gtp='gator'
nc=ncp='ncx'
tb='turbo'
ovd='override'
fr='freak'
m2='mach2'          #to write it prettier time will come shall i say
"""                 #second way is better, but you can make it cleaner

exclusiveModels = {'fr', 'm3', 'tb'}
modelsMap = {'bl': 'Blade', 'blp': 'Blade', 's1': 'S1', 's1p': 'S1', 'gt': 'Gator', 'gtp': 'Gator', 'nc': 'NCX', 'ncp': 'NCX', 'tb': 'Turbo', 'ovd': 'Overdrive', 'fr': 'Fr33k', 'm3': 'Mach3'}
                    #have to find cleaner way for double keys for one value
                    #and exclusive models. double sign for premium: fr, m2, tb

premiumSet = {'blp', 's1p', 'gtp', 'ncp', 'tb2', 'ovd', 'fr', 'm3'}      #find better way for premium codes with 2 letters

blSizeSet={'30', '33', '35', '37', '40', '42', '45', '47', '50', '53'}    #have to update this shit
s1SizeSet={"36", "40", "44", "48", "52"}
frSizeSet=s1SizeSet
gtSizeSet={'55', '57', '60', '65', '70', '75'}
ncSizeSet={'60', '65', '70', '75'}
tbSizeSet=ncSizeSet
ovdSizeSet={'62', '70', '78', '86'}
m3SizeSet={'50', '55', '62', '70', '78', '86'}

modelToDict = {'Blade': blSizeSet, 'Gator': gtSizeSet, 'Fr33k': s1SizeSet, "S1": s1SizeSet, "NCX" : ncSizeSet, "Turbo": tbSizeSet, "Overdrive" : ovdSizeSet, "Mach3": m3SizeSet}
