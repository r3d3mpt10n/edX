class AdoptionCenter(object):

	def __init__(self, name, species_types, location):

		self.species_types = species_types
		
		self.name = name
		
		
		loc=list(location)
    		loc[0]=loc[0]+1.0-1.0
    		loc[1]=loc[1]+1.0-1.0
    		t = tuple(loc)
    		self.location = t
		
		

	def get_name(self):

		return(self.name)
		

	def get_location(self):
		
		return(self.location)


	def get_species_type(self):
		
		return(self.species_types.copy())

	def get_species_count(self):
		N = dict(filter(lambda (a,bc): bc>0, self.species_types.items()))
		return(N)

	def get_number_of_species(self, species_name):

		for keys,values in self.species_types.items():
			if keys == species_name:
				return(values)

	
	def adopt_pet(self,species_name):
      		if ( self.species_types.get(species_name) >0):
        		self.species_types[species_name]=self.species_types[species_name]-1


class Adopter(object):
	name=''
	desired_species=''
	def __init__(self, name, desired_species):
	        self.name=name
	        self.desired_species=desired_species

	def get_name(self):
	        return self.name

	def get_desired_species(self):
	        return self.desired_species

        def get_score(self,adoption_center):
    	    score=1.0*adoption_center.get_number_of_species(self.desired_species)
    	    return score

class FlexibleAdopter(Adopter,object):
    considered_species=[]


    def __init__(self, name, desired_species, considered_species):
        super(FlexibleAdopter,self).__init__(name, desired_species)
        self.considered_species=considered_species

    def get_score(self,adoption_center):
        s1=super(FlexibleAdopter, self).get_score(adoption_center)
        s2=0
        for k in self.considered_species:
            N = adoption_center.get_number_of_species(k)
            if N is None:
                N=0
            s2=s2+0.3*N
	    scr = s1+s2
        return scr

class FearfulAdopter(Adopter,object):
	feared_species =''
   	def __init__(self, name, desired_species, feared_species):
		super(FearfulAdopter,self).__init__(name, desired_species)
      	        self.feared_species=feared_species        

        def get_score(self,adoption_center):
		s1=super(FearfulAdopter, self).get_score(adoption_center)
                s2=adoption_center.get_number_of_species(self.feared_species)

		if s2 is None:
			s2=0

        	scr=s1-0.3*s2

        	if scr <0:
            		return 0.0
        	else:
            		return scr

class AllergicAdopter(Adopter):
    

   
	def __init__(self, name, desired_species, allergic_species):
	        Adopter.__init__(self, name, desired_species)
	        self.allergic_species = allergic_species
 
        def get_score(self, adoption_center):
        	for species in self.allergic_species:
        	    if adoption_center.get_species_count().get(species, 0) > 0:
        	        return 0.0
        	return Adopter.get_score(self, adoption_center)
 
 
class MedicatedAllergicAdopter(AllergicAdopter):


    	def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        	AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        	self.medicine_effectiveness = medicine_effectiveness
 
        def get_score(self, adoption_center):
        	min_med_effect = 1.0
        	for species in self.allergic_species:
        	    if species in adoption_center.get_species_count():
        	        med_effect = self.medicine_effectiveness.get(species, 0)
        	        if med_effect < min_med_effect:
        	            min_med_effect = med_effect
        	return Adopter.get_score(self, adoption_center) * min_med_effect


class SluggishAdopter(Adopter):

	def __init__(self, name, desired_species, location):
	        Adopter.__init__(self, name, desired_species)
	        self.location = location
 
	def get_linear_distance(self, to_location):
	        import math
	        return math.sqrt((to_location[0] - self.location[0])**2 + (to_location[1] - self.location[1])**2)
 
	def get_score(self, adoption_center):
	        import random
	        distance = self.get_linear_distance(adoption_center.get_location())
	        if distance < 1:
	            return 1 * Adopter.get_score(self, adoption_center)
	        if 1 <= distance < 3:
	            return random.uniform(0.7, 0.9) * Adopter.get_score(self, adoption_center)
	        if 3 <= distance < 5:
	            return random.uniform(0.5, 0.7) * Adopter.get_score(self, adoption_center)
	        if distance >= 5:
	            return random.uniform(0.1, 0.5) * Adopter.get_score(self, adoption_center)

	def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):

	    def get_score_key(x):
	        return adopter.get_score(x)
	    def get_name_key(x):
	        return x.get_name()
	    s = sorted(list_of_adoption_centers, key=get_name_key)
	    return sorted(s, key=get_score_key, reverse=True)
 
	def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
	
        def get_score_key(x):
        	return x.get_score(adoption_center)
    	def get_name_key(x):
        	return x.get_name()
    	s1 = sorted(list_of_adopters, key=get_name_key)
    	s2 = sorted(s1, key=get_score_key, reverse=True)
    	if n > len(s2): return s2
    	return s2[:n + 1]



ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2}, (1,1))
ab = AdoptionCenter("Place2", {"Mouse": 18, "Dog": 2}, (1,1))

ab.adopt_pet("Mouse")
print(ab.get_number_of_species("Mouse"))

