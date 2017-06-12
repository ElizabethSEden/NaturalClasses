import json
import itertools

class NaturalClasses:
    featureCombo_to_segments = dict()
    segmentList_to_featureCombos = dict()

    def __init__(self, map, limit_of_combinations):
        self.map = map
        self.featureCombo_to_segments = dict()
        empty_combination = []
        # generate combination of features
        for combo in map.combinations(limit_of_combinations):
            segments = map.get_segments_with_feature_value(combo)
            if segments is not None:
                self.featureCombo_to_segments[json.dumps(combo)] = [s for s in segments.keys()]
        #for each unique combination of segments, find the feature combinations which produce them
        for segment_list in set([str(segments) for segments in self.featureCombo_to_segments.values()]):
            self.segmentList_to_featureCombos[segment_list] = [key for key, value in
                                                               self.featureCombo_to_segments.items()
                                                               if str(value) == segment_list]

    def output(self, f):
        f.write("{")
        for key, value in self.segmentList_to_featureCombos.items():
            if value:
                f.writelines('\n{}:{},'.format(key, value))
        f.write("\n}")


    def output_redundant(self, f):
        for key, value in self.segmentList_to_featureCombos.items():
            if len(value) > 1:
                f.writelines('\n{}:{},'.format(key, value))

    def output_redundant_sans_subsets(self, f):
        for key, value in self.segmentList_to_featureCombos.items():
            relevant_classes = self.non_subset_redundancies(value)
            if len(relevant_classes) > 1 and not key == "[]":
                f.writelines('\n{}:{},'.format(key, relevant_classes))

    def output_redundant_if_nonsubsets(self, f):
        for key, value in self.segmentList_to_featureCombos.items():
            relevant_classes = self.non_subset_redundancies(value)
            if len(relevant_classes) > 1 and not key == "[]":
                f.writelines('\n{}:{},'.format(key, value))

    def non_subset_redundancies(self, classes):
        #return all dictionaries in list 'classes' that are not subsets of each other
        class_list = [json.loads(c) for c in classes]
        pairs_of_classes = itertools.combinations(class_list, 2)
        to_remove = []
        for pair in pairs_of_classes:
            if set(pair[0].items()).issubset(set(pair[1].items())):
                to_remove.append(pair[1])
            elif set(pair[1].items()).issubset(set(pair[0].items())):
                to_remove.append(pair[1])
        for item in to_remove:
            if item in class_list:
                class_list.remove(item)
        return class_list

    def output_segment_contrasts(self, f):
        pairs_of_segments = itertools.combinations(self.map.segments, 2)
        for pair in pairs_of_segments:
            first = self.map.data[pair[0]]
            second = self.map.data[pair[1]]
            contrasts = []
            for feature_name in self.map.feature_names:
                if (not first[feature_name] == "underspecified") and \
                        (not second[feature_name] == "underspecified") and \
                        (not first[feature_name] == second[feature_name]):
                    contrasts.append(feature_name)
            f.write('\n{}:{},'.format(pair, contrasts))


