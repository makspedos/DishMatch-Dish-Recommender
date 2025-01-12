from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class RecommendAlgorithm:
    def cosine_recommend_by_title(self, dish_title, title_list):
        if len(title_list) >1 and dish_title:
            title_list.append(dish_title)
            vectorizer = TfidfVectorizer()
            vectorizer_dishes = vectorizer.fit_transform(title_list)

            similarities = cosine_similarity(vectorizer_dishes[-1], vectorizer_dishes[:-1]).flatten()
            print(similarities)
            sorted_indices = similarities.argsort()[::-1][:3]
            recommendation = [title_list[i] for i in sorted_indices]
            return recommendation

def get_user_preferences(user):
    return


if __name__ == '__main__':
    recipes = [
        "Tomato Soup",
        "Chicken Noodle Soup",
        "Creamy Mushroom Soup",
        "Minestrone Soup",
        "Vegetable Lentil Soup",
        "Beef Barley Soup",
        "Split Pea Soup",
        "Potato Leek Soup",
        "Chicken dish"
        ]
    value = 'Beef'
    recommended_title = RecommendAlgorithm()
    recommended_title.cosine_recommend_by_title(value, recipes)