import subprocess

models = ["standard_PGD_attack_n50.json",
          "standard_PGD_attack_n75.json",
          "standard_PGD_attack_n100.json",
          "standard_PGD_attack_n150.json",
          "standard_PGD_attack_n200.json"]

for model in models:
    print("#######################################################################################################")
    print(f"Training model with: n_steps={model[-8:-5]}:")
    run_fid = subprocess.run(["python", "bpda_eot_attack.py", "--config_file", f"./config_attack/{model}"])
    print("#######################################################################################################")
    print("   ")