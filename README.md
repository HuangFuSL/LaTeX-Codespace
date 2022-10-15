# LaTeX Codespace Template

This is a LaTeX Codespace Configuation Template, which is to create a working LaTeX environment as efficient as possible.

## Usage

1. Create your own repo using this repo as a template.
2. Setup codespace prebuilds in Settings/Codespace.
3. Wait for your codespace prebuilding task complete.
4. Create a codespace from the repo.

## Features

* Full TeX Live installation (see [here](https://github.com/qdm12/latexdevcontainer/blob/master/Dockerfile))
* `bibtex` support - automatically compile `.bib` files
* `latexindent` support - automatically formatting on save
* `texcount` support - automatically count words on save

Submit an issue if you believe an extension is essential to this environment.

### Extensions Included

* [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
* [GitLens — Git supercharged](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
* [Trailing Spaces](https://marketplace.visualstudio.com/items?itemName=shardulm94.trailing-spaces)
* [Rewrap](https://marketplace.visualstudio.com/items?itemName=stkb.rewrap)
* [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)
* [Material Theme](https://marketplace.visualstudio.com/items?itemName=Equinusocio.vsc-material-theme)

### Additional Packages

* libfont - required by XeLaTeX
* Python 3

## Customize

Configuration in `.devcontainer/Dockerfile` and `.devcontainer/devcontainer.json` are my usual usage. However, you can customize packages, extensions and setting in the following steps if needed.

### Add additional packages to your codespace

The image is based on Ubunut 20.04 LTS which uses `apt` and `apt-get` to manage packages. Just add the following code to `.devcontainer/Dockerfile` if you want to customize packages included in the prebuilt image.

```dockerfile
RUN apt-get update
RUN apt-get install your-package -y
```

### Add additional extensions to your codespace

Extensions and settings configuration are stored under `.devcontainer/devcontainer.json`. If you want to add your own extension, follow the following steps:

1. Find the extension in Visual Studio Code or in [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/VSCode)
2. Get the extension ID: In **Visual Studio Code**, right click on the extension and click "Copy Extension ID". In **Visual Studio Code Marketplace**, you have to go to the URL section of your browser, the extension ID is displayed in the following manner.

   ```
    https://marketplace.visualstudio.com/items?itemName=<extension-id>
   ```

3. Add the extension ID to the `extensions` field in `.devcontainer/devcontainer.json`.

   ```json
    "extensions": [
        ...
        "<extension-id>",
    ],
   ```

After these steps, you've successfully added an extension to the codespace. You may want to import your preferences from you local Visual Studio Code workspace.

### Import additional setting from `settings.json`

This step is relatively simple - just open your `settings.json` and copy the related settings entry to `settings` field in `.devcontainer/devcontainer.json`.

### Customizing themes and icon themes

First make sure you have added the theme in `extensions` entry. Update the `workbench.colorTheme` and `workbench.iconTheme` entry in `.devcontainer/devcontainer.json`.

## Acknowledgements

The template is based on [qdm12/latexdevcontainer](https://github.com/qdm12/latexdevcontainer).
