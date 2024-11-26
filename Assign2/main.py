import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import matplotlib.pyplot as plt
import os
class IrisDataFilter:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    def filter_by_species(self, species: str):
        filtered_data = self.data[self.data['Species'] == species]
        return filtered_data

    def get_feature_distribution(self, species: str, feature: str):
        filtered_data = self.filter_by_species(species)
        return filtered_data[feature]

app = FastAPI()
iris_data_filter = IrisDataFilter('C:\Sanika\Python\MLOPS\iris.csv')  # Replace with the correct path to your dataset


@app.get("/filter/")
def filter_iris_data(species: str):
    filtered_data = iris_data_filter.filter_by_species(species)
    if filtered_data.empty:
        raise HTTPException(status_code=404, detail="Species not found")
    return filtered_data.to_dict(orient='records')


@app.get("/visualize/")
def visualize_feature_distribution(species: str, feature: str):
    feature_data = iris_data_filter.get_feature_distribution(species, feature)
    if feature_data.empty:
        raise HTTPException(status_code=404, detail="Species or feature not found")

    plt.figure(figsize=(8, 6))
    plt.hist(feature_data, bins=20, alpha=0.7, color='b', edgecolor='black')
    plt.title(f'{feature.capitalize()} Distribution for {species.capitalize()}')
    plt.xlabel(feature.capitalize())
    plt.ylabel('Frequency')
    plt.grid(True)

    image_path = f"{species}_{feature}_distribution.png"
    plt.savefig(image_path)
    plt.close()

    return FileResponse(image_path, media_type="image/png", filename=image_path)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
