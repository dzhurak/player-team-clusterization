# Workshop: Person Classification in Sports

#### Pre-requirements

- python 3.6
- pip
- conda (_Windows users_)

#### Requirements

Install requirements:

```bash
pip install -r requirements.txt
```

Download data:

[groups_to_cluster_from_tracker.tar.gz](https://drive.google.com/file/d/1sjMRPO6NnZC_UmQEmo7Q3ozehiZUS6J0/view?usp=sharing)

[team_color_dataset_splitted.tar.gz](https://drive.google.com/file/d/18B1iEDN282STqfbjIbvxbdOFV0oNjs3l/view?usp=sharing)

```bash
cd player-team-clusterization
tar -xvzf team_color_dataset_splitted.tar.gz
tar -xvzf groups_to_cluster_from_tracker.tar.gz
```

---

#### Diving into details (for beginners):

**Linux**

- Install python3.6:

```bash
mkdir /tmp/Python36
cd /tmp/Python36

sudo wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz
sudo tar xzf Python-3.6.6.tgz
cd /tmp/Python36/Python-3.6.6/
sudo ./configure
sudo make altinstall
```

- Return to folder with workshop sources:

```bash
python3.6 -m venv ./workshop
source workshop/bin/activate
```

- Add python3.6 kernel to Jupyter

```bash
pip install jupyter
python3.6 -m pip install ipykernel
python3.6 -m ipykernel install --user
```

**Windows**

- Install [Anaconda](https://www.anaconda.com/download/)

---
**Contributors:** Raid Arfua, Bogdan Zhurakovskyi

**Speakers:**

Raid Arfua (github: [arfua](https://github.com/Arfua), skype: raid_arfua)

Bogdan Zhurakovskyi (github: [dzhurak](https://github.com/dzhurak), skype: zhurak)
