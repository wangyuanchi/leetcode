class Node:
    def __init__(self, rating: int, food: str):
        self.rating = rating
        self.food = food

    def __lt__(self, other: Node):
        if self.rating < other.rating:
            return True
        elif self.rating > other.rating:
            return False
        else:
            return self.food > other.food
        
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_rating = {}
        self.food_to_cuisine = {}
        self.cuisine_to_heap = {}

        for i in range(len(foods)):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.food_to_rating[food] = rating
            self.food_to_cuisine[food] = cuisine
            if cuisine not in self.cuisine_to_heap:
                self.cuisine_to_heap[cuisine] = []
            self.cuisine_to_heap[cuisine].append(Node(rating, food))

        for cuisine, heap in self.cuisine_to_heap.items():
            heapq.heapify_max(self.cuisine_to_heap[cuisine])

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating[food] = newRating
        heapq.heappush_max(
            self.cuisine_to_heap[self.food_to_cuisine[food]],
            (Node(newRating, food))
        )

    def highestRated(self, cuisine: str) -> str:
        while (
            self.food_to_rating[self.cuisine_to_heap[cuisine][0].food]
            != self.cuisine_to_heap[cuisine][0].rating
        ):
            heapq.heappop_max(self.cuisine_to_heap[cuisine])

        return self.cuisine_to_heap[cuisine][0].food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)