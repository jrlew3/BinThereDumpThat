from image_model import * 
from PIL import Image
from pathlib import Path

data_dir  = 'dataset/GarbageClassification/GarbageClassification'
classes = os.listdir(data_dir)

# apply transformations to the data set and import it 
transformations = transforms.Compose([transforms.Resize((256, 256)), transforms.ToTensor()])
dataset = ImageFolder(data_dir, transform = transformations)

# loading and splitting data 
random_seed = 42
torch.manual_seed(random_seed)

train_ds, val_ds, test_ds = random_split(dataset, [1593, 176, 758])
batch_size = 32

train_dl = DataLoader(train_ds, batch_size, shuffle = True, num_workers = 4, pin_memory = True)
val_dl = DataLoader(val_ds, batch_size*2, num_workers = 4, pin_memory = True)

device = get_default_device()

train_dl = DeviceDataLoader(train_dl, device)
val_dl = DeviceDataLoader(val_dl, device)
to_device(model, device)

model = ResNet(dataset)

model = to_device(ResNet(dataset), device)
evaluate(model, val_dl)

# start training mode 
num_epochs = 8
opt_func = torch.optim.Adam
lr = 5.5e-5

history = fit(num_epochs, lr, model, train_dl, val_dl, opt_func)

plot_accuracies(history)
plot_losses(history)

img, label = test_ds[17]
plt.imshow(img.permute(1, 2, 0))
print('Label:', dataset.classes[label], ', Predicted:', predict_image(img, model))

loaded_model = model

predict_external_image('cans.jpg', loaded_model)