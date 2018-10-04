import torch


def get_torch_device(random_seed=12345):
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(random_seed)
        return torch.device("cuda:0")
    torch.manual_seed(random_seed)
    return torch.device("cpu")


def to_bgr_transform(tensor):
    return tensor[[2, 1, 0], :, :]


def same_padding(kernel_size):
    return tuple((k - 1) // 2 for k in kernel_size)


def valid_padding(kernel_size):
    return tuple(0 for _ in kernel_size)
