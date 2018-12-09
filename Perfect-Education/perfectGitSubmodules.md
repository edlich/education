Git Submodules
--------------

Use submodules to integrate dependencies into your repository.
You can point either to a specific version or a branch or leave the repository to decide for itself.

You can create in your repository a `.gitmodules` file:

```
[submodule "foldername"]
      path = foldername
      url = git://github.com/sampleuser/samplerepo.git
```

To add a second submodule append (this time referencing a specfic branch)

```
[submodule "foldername2"]
      path = foldername2
      url = git://github.com/sampleuser/samplerepo2.git
      branch = stable
```

Sometimes a newly added submodule via file is not yet recognized automatically, so you have to add it using the git command:
```
git submodule add foldername git://github.com/sampleuser/samplerepo.git
```

To update all submodules in youre repository run 
```
git submodule update --recursive
```
