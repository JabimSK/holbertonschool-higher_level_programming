#.items():

                if k == "id":
                    
                    if v is None:
                        
                        self.__init__(self.width, self.height, self.x, self.y)
                        
                    else:
                        
                        self.id = v
                        
                elif k == "width":
                    
                    self.width = v
                    
                elif k == "height":
                    
                    self.height = v
                    
                elif k == "x":
                    
                    self.x = v
                    
                elif k == "y":
                    
                    self.y = v
                    

                    
    def to_dictionary(self):
        
        """Return the dictionary representation of a Rectangle."""
        
        return {
            
            "id": self.id,
            
            "width": self.width,
            
            "height": self.height,
            
            "x": self.x,
            
            "y": self.y
            
        }
    

    
    def __str__(self):
        
        """Return the print() and str() representation of the Rectangle."""
        
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       
                                                       self.x, self.y,
                                                       
                                                       self.width, self.height)
