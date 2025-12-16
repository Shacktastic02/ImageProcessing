from PIL import Image
import os

class Sample:
    def __init__(self, features, label):
        self.features = features
        self.label = label

class Perceptron:
    def __init__(self, weights):
        self.weights = weights

    def GetMainWeights(self):
        return self.weights[:-1]
    
    def GetBias(self):
        return self.weights[-1]
    
samples = []

for num in [0,1]:
    path = f"./{num}/"
    files = os.listdir(path)
    for i in range(1):
        filePath = path + files[i]
        img = Image.open(filePath)
        rast = img.load()

        sum = 0
        for y in range(img.height):
            for x in range(img.width):
                pix = rast[x,y]
                sum += pix
        
        avg = sum / (img.height*img.width)
        samples.append(Sample([avg],num))

print(samples)
print(samples[0].features)
print(samples[1].features)

perc = Perceptron([0,0])

def GuessLabel(s,p):
    feats = s.features
    weights = p.GetMainWeights()
    sum = 0
    for i in range(len(feats)):
        sum += feats[i] * weights[i]
    sum += p.GetBias()
    return 0 if sum < 0 else 1

print(GuessLabel(samples[0], perc))
print(GuessLabel(samples[1], perc))

epochs = 0
rate = .1

for epoch in epochs:
    for sample in samples[:-1]:
        predictedLabel = GuessLabel(sample, perc)
        if predictedLabel != sample.label:
            feats = sample.features
            weights = perc.GetMainWeights()
            for i in range(len(feats)):
                perc.weights[i] += (sample.label - predictedLabel)*rate*feats[i]
            perc.weights[-1] += (sample.label - predictedLabel)*rate
    print(perc.weights)

print(GuessLabel(samples[0], perc))
print(GuessLabel(samples[1], perc))
print(GuessLabel(samples[-1], perc))