# -*- coding: utf-8 -*-
#
# Developed by Haozhe Xie <cshzxie@gmail.com>
# Adapted from: https://github.com/hzxie/Pix2Vox


import torch


class Decoder(torch.nn.Module):
    def __init__(self, cfg):
        super(Decoder, self).__init__()
        self.cfg = cfg

        # Layer Definition
        self.layer1 = torch.nn.Sequential(
            torch.nn.ConvTranspose3d(2048, 512, kernel_size=4, stride=2, bias=cfg['tconv_use_bias'], padding=1),
            torch.nn.BatchNorm3d(512),
            torch.nn.ReLU()
        )

        self.layer2 = torch.nn.Sequential(
            torch.nn.ConvTranspose3d(512, 128, kernel_size=4, stride=2, bias=cfg['tconv_use_bias'], padding=1),
            torch.nn.BatchNorm3d(128),
            torch.nn.ReLU()
        )

        self.layer3 = torch.nn.Sequential(
            torch.nn.ConvTranspose3d(128, 32, kernel_size=4, stride=2, bias=cfg['tconv_use_bias'], padding=1),
            torch.nn.BatchNorm3d(32),
            torch.nn.ReLU()
        )
        self.layer4 = torch.nn.Sequential(
            torch.nn.ConvTranspose3d(32, 8, kernel_size=4, stride=2, bias=cfg['tconv_use_bias'], padding=1),
            torch.nn.BatchNorm3d(8),
            torch.nn.ReLU()
        )
        self.layer5 = torch.nn.Sequential(
            torch.nn.ConvTranspose3d(8, 1, kernel_size=1, bias=cfg['tconv_use_bias']),
            torch.nn.Sigmoid()
        )

    def forward(self, image_features):
        image_features = image_features.permute(1, 0, 2, 3, 4).contiguous()
        image_features = torch.split(image_features, 1, dim=0)
        gen_volumes = []
        raw_features = []

        for features in image_features:
            gen_volume = features.view(-1, 2048, 2, 2, 2)
            gen_volume = self.layer1(gen_volume)
            gen_volume = self.layer2(gen_volume)
            gen_volume = self.layer3(gen_volume)
            gen_volume = self.layer4(gen_volume)
            raw_feature = gen_volume
            gen_volume = self.layer5(gen_volume)
            raw_feature = torch.cat((raw_feature, gen_volume), dim=1)

            gen_volumes.append(torch.squeeze(gen_volume, dim=1))
            raw_features.append(raw_feature)

        gen_volumes = torch.stack(gen_volumes).permute(1, 0, 2, 3, 4).contiguous()
        raw_features = torch.stack(raw_features).permute(1, 0, 2, 3, 4, 5).contiguous()

        return raw_features, gen_volumes
