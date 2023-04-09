# Factory class for ADT's
class ADTFactory:
    def getADT(type):
        from .Datastructuren.ARNE.Wrappers.twoThreeTable import TwoThreeTreeTable as Table
        from .Datastructuren.ARNE.Wrappers.PrioQueue import PriorityQueue as Queue
        from .Datastructuren.ARNE.Datatypes.LinkedList import LinkedList
        """
        Returns the proper datastructure corresponding to the input parameter

        possible inputs:
            -"User"\n
            -"Movie" \n
            -"Room" \n
            -"Tickets" \n
            -"Events" \n
            -"Timestamps" \n

        Pre-condition: /
        Post-condition: returns the proper datastructure
        """
        ADTDict = {
            "User": Table,
            "Movie": Table,
            "Screening": Table,
            "Room": Table,
            "Tickets": Table,
            "Events": Queue,
            "Timestamps": Table,
            "NonUniqueList": LinkedList
        }
        if type != "Events":
            return ADTDict[type]()
        else:
            return ADTDict[type](maxQueue=False)


class SearchKeyFactory:
    def getSearchkey(type):
        from .User import User
        from .Movie import Movie
        from .Room import Room
        from .Screening import Screening
        """
        -> "User"
        -> "Movie"
        -> "Room"
        -> "Screening"
        """
        d = {
            "User" : User.getId,
            "Movie" : Movie.getId,
            "Screening" : Screening.getId
        }
        return d[type]