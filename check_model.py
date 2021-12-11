import torch

weights = 'best.pt'
ckpt = torch.load(weights)
model = ckpt['model']
print(model.yaml['anchors'])