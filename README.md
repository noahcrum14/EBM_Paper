# BPDA + EOT PGD Whitebox Attack for Saved Nets

This repository implements a whitebox adversarial attack that combines Backward Pass Differentiable Approximation (BPDA) and Expectation Over Transformation (EOT) with Projected Gradient Descent (PGD). The attack is designed for pre-trained networks and includes a purification step via an Energy-Based Model (EBM).

Below is an overview of the codebase, setup instructions, file descriptions, usage details, and customization options.

---

## Overview

The main goal of this codebase is to generate adversarial examples against a pre-trained classifier (implemented as a WideResNet) while employing an EBM-based purification mechanism. The attack pipeline involves:
- Loading experiment configurations from JSON files.
- Importing and normalizing image datasets (CIFAR10, CIFAR100, or SVHN).
- Loading pre-trained models (classifier and optionally an EBM).
- Performing iterative adversarial attacks using PGD with BPDA and EOT strategies.
- Logging results, including defense accuracy over multiple attack iterations and saving adversarial examples.

---

## Requirements

- **Python 3.x**
- **PyTorch** and **Torchvision**
- **Matplotlib**
- **tqdm**
- Other standard libraries: `argparse`, `json`, `datetime`, `os`

To install the required packages, run:

```bash
pip install torch torchvision matplotlib tqdm
```

---

## File Descriptions

### bpda_eot_attack.py  
This is the main script that executes the adversarial attack. It:
- Loads the experiment configuration from a JSON file (via the `--config_file` argument).
- Sets up the experiment environment (directories, logging, seed, etc.) using utility functions.
- Loads the dataset and pre-trained models (classifier and, if applicable, EBM).
- Implements key functions:
  - **Purification:** Uses iterative Langevin MCMC updates to purify adversarial examples.
  - **EOT Prediction & Loss:** Averages over multiple stochastic predictions for robust attack gradient computation.
  - **PGD Updates:** Generates adversarial examples by iteratively updating inputs within a constrained norm ball.
- Logs and saves intermediate results and plots defense accuracy over attack iterations.

*(See citeturn0file0 for complete code details.)*

---

### ebm_def_auto_attack_PGD.py  
This helper script automates running the attack across multiple configurations. It:
- Iterates over a predefined list of configuration files (e.g., `"standard_PGD_attack_n50.json"`, `"standard_PGD_attack_n75.json"`, etc.).
- Executes the `bpda_eot_attack.py` script for each configuration using subprocess calls.
- Provides clear console output to track progress across different attack settings.

*(Refer to citeturn0file1 for the implementation.)*

---

### nets.py  
This file contains the model definitions:

- **EBM (Energy-Based Model):**  
  A lightweight network that applies a series of convolutional layers and LeakyReLU activations to compute energy scores. It is used for the purification step during the attack.

- **WideResNet (Wide Residual Network):**  
  An implementation of WideResNet adapted from the original work. It is used as the classifier against which adversarial examples are generated.

*(Full details in citeturn0file2.)*

---

### utils.py  
Utility functions that support the experimental setup:
- **setup_exp:**  
  Creates experiment directories, sets the random seed for reproducibility, and saves copies of code files for future reference.

- **import_data:**  
  Loads and normalizes datasets (CIFAR10, CIFAR100, or SVHN) with transformations that scale pixel intensities to the range `[-1, 1]`.

*(See citeturn0file3 for the complete code.)*

---

## Usage

### Running a Single Attack

To execute the BPDA + EOT PGD attack, run:

```bash
python bpda_eot_attack.py --config_file <path_to_config_json>
```

The configuration JSON should include parameters such as:
- **exp_dir:** Base directory for saving experiment results.
- **seed:** Random seed for reproducibility.
- **data_type:** Dataset to use (e.g., `"cifar10"`, `"cifar100"`, or `"svhn"`).
- **batch_size**, **subset_shuffle**, and other data loading parameters.
- **clf_weight_path:** Path to the pre-trained classifier weights.
- **ebm_weight_path:** Path to the pre-trained EBM weights (if using purification).
- **Attack parameters:** Such as `adv_eps`, `adv_eta`, `adv_steps`, and EOT/BPDA specific settings.

### Running Multiple Attacks

To run multiple experiments with different settings, execute the automation script:

```bash
python ebm_def_auto_attack_PGD.py
```

This script will loop over several configuration files and run the attack for each, printing progress information to the console.

---

## Experiment Workflow

1. **Setup:**  
   The experiment directory is created with a unique timestamp. Code files are saved, and the random seed is set for reproducibility.

2. **Data Loading:**  
   The selected dataset is loaded, transformed, and normalized.

3. **Model Loading:**  
   Pre-trained weights for both the classifier (WideResNet) and the EBM (if applicable) are loaded.

4. **Attack Execution:**  
   Adversarial examples are generated iteratively using PGD. Depending on the configuration, BPDA and EOT methods are applied to refine the attack.

5. **Evaluation and Logging:**  
   The accuracy of the defense is evaluated over attack iterations. Intermediate results, final adversarial examples, and accuracy plots are saved to the experiment directory.

---

## Results and Outputs

- **Logs and Checkpoints:**  
  The experiment results, including original images, adversarial images, labels, and defense accuracy logs, are saved as a PyTorch checkpoint (e.g., `results.pth`) within the experiment directory.

- **Plots:**  
  An accuracy plot (`accuracy_over_attack.png`) is generated, showing how the defense accuracy changes over the attack iterations.

---

## Customization

- **Configuration:**  
  Modify the JSON configuration file to adjust experiment parameters (e.g., attack strength, number of attack steps, and EOT/BPDA settings).

- **Model Architecture:**  
  Update or extend the models in `nets.py` if you want to experiment with different network architectures.

- **Data Transformations:**  
  Adjust the transformations in `utils.py` to accommodate other datasets or to experiment with different normalization schemes.

---

## License

This codebase is provided under the MIT License. *(Update this section if using a different license.)*

---

## Acknowledgments

- The WideResNet implementation is adapted from [Bumsoo Kim's repository](https://github.com/meliketoy/wide-resnet.pytorch) with minor modifications.  
  *(See citeturn0file2)*
- This project leverages advanced adversarial attack techniques including BPDA and EOT to evaluate and improve network robustness.
