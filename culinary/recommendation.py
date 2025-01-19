from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
from collections import Counter
import random

class AssociationRecommender:
    def __init__(self, min_support=0.001, min_lift=2, min_threshold=0.01, num_itemsets=100):
        """
        Initializes the AssociationRecommender with specified parameters for pattern finding.

        Args:
            min_support (float): The minimum support threshold for the apriori algorithm.
            min_lift (int): The minimum lift threshold for filtering association rules.
            min_threshold (float): The minimum threshold for the association rules.
            num_itemsets (int): The number of itemsets to consider during pattern finding.
        """
        self.min_support = min_support
        self.min_threshold = min_threshold
        self.num_itemsets = num_itemsets
        self.min_lift = min_lift

    def template_method(self, ingredients):
        encoded_df = self.preprocessing(ingredients)
        rules = self.find_patterns(encoded_df)
        result_ingredients = self.examine_ingredients(rules)
        return result_ingredients

    def preprocessing(self, ingredients):
        encoder = TransactionEncoder()
        ingredients_encoded = encoder.fit(ingredients).transform(ingredients)
        df = pd.DataFrame(ingredients_encoded, columns=encoder.columns_)
        return df

    def find_patterns(self, df):
        frequent = apriori(df, min_support=self.min_support, use_colnames=True)
        generated_rules = association_rules(frequent, metric="lift", min_threshold=self.min_threshold,
                                            num_itemsets=self.num_itemsets)
        if df.shape[0] > 1:
            generated_rules = generated_rules[generated_rules['lift'] >= self.min_lift]
        return generated_rules

    def examine_ingredients(self, rules):
        ingredients = [ingredient for rule in rules['antecedents'] for ingredient in rule]
        random.shuffle(ingredients)
        antecedents_count = Counter(ingredients)
        antecedents_count = antecedents_count.most_common()[:3]
        return antecedents_count

    def get_user_preferences(self, user):
        ingredients = []
        for dish in user['user_dish']:
            ingredients.append(dish['ingredients'])
        result = self.template_method(ingredients)
        return result


if __name__ == '__main__':
    train_data = {'user_dish': [

        {
            "ingredients": ["Tomato", "Onion", "Garlic"],
        },
        {
            "ingredients": ["Onion", "Cheese", "Bread"],
        },
        {
            "ingredients": ["Avocado", "bananas", "Tomato"],
        },
        {
            "ingredients": ["Avocado", "Lettuce", "Tomato"],
        },
        {
            "ingredients": ["Eggs", "Cheese", "Peas"],
        },
    ]}

    recommend = AssociationRecommender()
    result = recommend.get_user_preferences(train_data)
    print(result)

