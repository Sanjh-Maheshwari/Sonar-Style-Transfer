# Sonar-Style-Transfer

Exploring application of computer vision in domain of sonar imaging. 

## Table of Contents
* [Introduction](#intro)
* [Acknowledgements](#ackn)
* [Tasks](#tasks)
* [Dataset](#dataset)
* [Modelling](#training)
* [Style Transfer](#nst)
* [Evaluation](#eval) 

## Introduction <a name="intro"></a> 

The application of computer vision in domain of sonar imaging is very limited due to insufficient public sonar image datasets. 
Availability of a large-scale sonar dataset would enable applications like underwater object detection, mine detection etc. 
The main goal of this work is to create a large-scale synthetic dataset of sonar images using synthetic images of underwater like objects generated using 3D modelling softwares and then using Neural Style Transfer to transfer the style of real sonar images to synthtic images. This repo aims to provide script for the above tasks and extend to other sonar imaging tasks in future. 

## Acknowledgements <a name="ackn"></a> 

This project was made possible with previous contributions referenced below: 
<ol>
  <li> https://github.com/gordicaleksa/pytorch-neural-style-transfer </li>
  <li> https://github.com/mvaldenegro/marine-debris-fls-datasets </li>
</ol>

## Tasks <a name="tasks"></a>

We perform following tasks and also provide the code for the same : 

- [:heavy_check_mark:] [Scene Generation : **Blender**](/Scene%20Generation)  
- [:heavy_check_mark:] [Self Supervised Learning : **RotNet**](/Modelling)  
- [:heavy_check_mark:] [Style Transfer : **VGG19**](/Style%20Transfer) 
- [:heavy_check_mark:] [Evaluation : **FID**](/Evaluation)  
- [:white_circle:] [Multi Image Style Transfer](/)  

Further tasks will be added in the future according to progress of the project. 

## Dataset <a name="dataset"></a> 

We use various 3D models of objects like ships and airplanes from the web to generate synthetic data using Blender. 
For pretraining of VGG-19 using RotNet methodoly we make use of [**Forward-Looking Sonar Marine Debris Datasets**](https://github.com/mvaldenegro/marine-debris-fls-datasets) combined with dataset of submerged ships and aeroplanes. 

## Modelling <a name="training"></a> 

## Style Transfer <a name="nst"></a> 

### Methodology 

### Parameters 

### Sample Script

## Evaluation <a name="eval"></a> 


