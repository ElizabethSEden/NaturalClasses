import itertools

class Map:
    #Data is a dictionary of segment to dictionary of feature name to feature value
    def __init__(self, data):
        self.data = data
        self.segments = data.keys()
        self.feature_names = self.get_features()
        self.values = self.get_values()

    def get_features(self):
        feature_list = []
        for segment, features in self.data.items():
            for feature in features:
                if feature not in feature_list:
                    feature_list.append(feature)
        return feature_list

    def get_values(self):
        values = []
        for segment, features in self.data.items():
            for value in features.values():
                if value not in values:
                    values.append(value)
        return values

    def combinations(self, number_of_features_to_combine):
        feature_combinations = self.get_combinations_of_features(number_of_features_to_combine)
        combos = []
        values = [v for v in self.values if not v == "underspecified"]
        for feature_combination in [list(f) for f in feature_combinations]:
            combos.extend([dict(zip(feature_combination, comb)) for comb in itertools.product(values, repeat=len(feature_combination))])
        return combos

    def get_combinations_of_features(self, total_number_of_features_to_combine = None):
        feature_combinations = []
        if total_number_of_features_to_combine is None:
            total_number_of_features_to_combine = len(self.feature_names) + 1
        for number_of_features in range(total_number_of_features_to_combine):
            feature_combinations.extend(itertools.combinations(self.feature_names, number_of_features))
        return list(filter(None, feature_combinations))

    def get_segments_with_feature_value(self, dict):
        segments = self.data
        for feature, value in dict.items():
            matching_segments = {}
            for segment, feature_values in segments.items():
                if feature_values[feature] == value:
                    matching_segments[segment] = feature_values
            segments = matching_segments
        return segments