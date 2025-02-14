import os
import pandas as pd
import whylogs as why
from whylogs.core import DatasetProfileView

# 创建一个示例 DataFrame
data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "salary": [50000, 60000, 70000, 80000],
}
df = pd.DataFrame(data)

# 使用 whylogs 对 DataFrame 进行 profiling
profile = why.log(df)

# 查看 profiling 结果
profile_view = profile.view()
print(profile_view.to_pandas())


os.makedirs("profiles", exist_ok=True)

profile.writer("local").option(base_dir="profiles").write(dest="sample.bin")
# If you want, you can also not specify a dest, but an optional base_dir,
# which will write your profile with its timestamp to this base directory you want.
# profile.writer("local").option(base_dir="profiles").write()


# Load the DatasetProfileView from the file
loaded_profile_view = DatasetProfileView.read("profiles/sample.bin")

# Inspect the loaded profile
print(loaded_profile_view.to_pandas())
