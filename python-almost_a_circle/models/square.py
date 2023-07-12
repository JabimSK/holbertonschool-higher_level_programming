#ize":

                    self.size = v
                    
elif k == "x":
    
                    self.x = v
                    
elif k == "y":
    
                    self.y = v
                    

                    
    def to_dictionary(self):
        
        """Return the dictionary representation of the Square."""
        
        return {
            
            "id": self.id,
            
            "size": self.width,
            
            "x": self.x,
            
            "y": self.y
            
        }
    

    
    def __str__(self):
        
        """Return the print() and str() representation of a Square."""
        
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 
                                                 self.width)
