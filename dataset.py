import os
import cv2
import numpy as np
import torch
from torch.utils.data import Dataset

class face_train_Dataset(Dataset):
    """
    データセット

    """

    def __init__(self, image_dir, image_name="shiraishi", transform=None):
        """
        初期化関数
        :param image_dir: 画像のルートディレクトリ
        """
        self.image_dir = image_dir
        self.image_name = image_name
        self.image_num = len(os.listdir(image_dir))
        self.tranform = transform

    def __len__(self):
        """
        データセットの総数を返す
        :return:
        """
        return self.image_num

    def __getitem__(self, idx):
        image_path = os.path.join(self.image_dir, self.image_name + str(idx) + ".jpg")
        image = cv2.imread(image_path)
        if self.transform:
            image = self.tranform(image)
        return image
