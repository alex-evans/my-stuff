
class Group:
    '''
    Group class handles all things dealing with what a Group can do
        Topic -> Group -> Card

    Attributes:
    ----------
        id = 

    Public Methods:
    ---------------

    '''

    def __init__(self, name):
        self.id = save_group_and_get_id(name)