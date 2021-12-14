class Iterator:
    items_list = []

    def __enter__(self):
        return self
    
    def __exit__(self, exception_type, exception_name, trace):
        try:
            return self.items_list.clear()
        except:
            raise AttributeError

    def __iter__(self):
        self.iteration_number = 0
        return self

    def __next__(self):
        if self.iteration_number < len(self.items_list):
            try:
                return self.items_list[self.iteration_number]
            except:
                raise StopIteration
            finally:
                self.iteration_number += 1
    
    def __getitem__(self, index):
        try:
            if isinstance(index, int):
                return self.items_list[index]
            if isinstance(index, slice):
                start = index.start
                stop = index.stop
                step = index.step
                if step is None:
                    step = 1
                if stop is None:
                    if step is None and step < 0:
                        stop = 0
                    else:
                        stop = len(self.items_list) - 1
                if start is None:
                    if step is None and step < 0:
                        start = len(self.items_list) - 1
                    else:
                        start = 0
                return [el for el in self.items_list[start:stop:step]]
        except:
             IndexError("ERROR!!! Invalid index or index type")
    
    def display_item(self, element):
            print('*' * 60)
            print("*{:^58}*".format(element))
            print('*' * 60)