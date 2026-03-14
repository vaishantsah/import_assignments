#Please write a program to generate all sentences where subject is in ["I", "You"] and
#verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
class SentenceGenerator:
    def __init__(self, subjects, verbs, objects):
        self.subjects = subjects
        self.verbs = verbs
        self.objects = objects

    def generate_sentences(self):
        sentences = []
        for subject in self.subjects:
            for verb in self.verbs:
                for obj in self.objects:
                    sentences.append(f"{subject} {verb} {obj}")
        return sentences

if __name__ == "__main__":
    subjects = ["I", "You"]
    verbs = ["Play", "Love"]
    objects = ["Hockey", "Football"]

    generator = SentenceGenerator(subjects, verbs, objects)
    all_sentences = generator.generate_sentences()
    
    for sentence in all_sentences:
        print(sentence)