from dp_cgans import DP_CGAN
import pandas as pd

tabular_data = pd.read_csv('Notebooks/test_datasets/processed_diabetes_data.csv')

model = DP_CGAN(
   epochs=2,  # number of training epochs
   batch_size=30,  # the size of each batch
   log_frequency=True,  # log model training details
   verbose=True,  # print detailed logs
   generator_dim=(64, 64, 64),  # dimensions of generator network
   discriminator_dim=(64, 64, 64),  # dimensions of discriminator network
   generator_lr=2e-4,  # learning rate for the generator
   discriminator_lr=2e-4,  # learning rate for the discriminator
   discriminator_steps=1,  # number of discriminator updates per generator update
   private=False  # whether to apply differential privacy
)


print("Start training model")
model.fit(tabular_data)
model.save("Notebooks/test_datasets/generator_diabetes.pkl")

# Generate 100 synthetic rows
syn_data = model.sample(200)
syn_data.to_csv("Notebooks/test_datasets/syn_data_diabetes.csv")