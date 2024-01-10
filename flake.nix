{
  inputs.nixpkgs.url = github:NixOS/nixpkgs/nixos-23.11;

  outputs = { self, nixpkgs, }:
    let
      supportedSystems = [ "x86_64-linux" "x86_64-darwin" "aarch64-darwin" ];
      forAllSystems = f: nixpkgs.lib.genAttrs supportedSystems (system: f system);

    in
      {
        devShell = forAllSystems (system:

          let
            pkgs = nixpkgs.legacyPackages.${system};
          in
            pkgs.mkShell {

              buildInputs =
              [

                # latex environment
                (
                  pkgs.texlive.combine {
                    inherit (pkgs.texlive)
                    scheme-full;
                  }
                )

                # python environment
                (
                  pkgs.python3.withPackages (p: [
                    p.numpy
                    p.pandas
                    p.matplotlib
                    p.ipython
                    p.notebook
                    p.pygments # for minted
                    p.colorful
                    p.flask
                    p.ruamel_yaml
                    p.pytest
                    p.scikit-learn
                  ])
                )

                # ruby environment
                (
                  pkgs.ruby_3_2.withPackages (p: [
                    p.jekyll
                    p.github-pages
                    p.webrick
                  ])
                )

                pkgs.coreutils
                pkgs.gnused
                pkgs.bash
                pkgs.fish
                pkgs.fd
                pkgs.zip
                pkgs.unzip
                pkgs.git
                pkgs.jq
                pkgs.yq
                pkgs.imagemagick

              ];

              # we export the path to the latex style files here this could be
              # done in texlive.combine above, but changes to the style files
              # would cause a long rebuild of the latex package
              shellHook = ''
                # add scripts to path
                export PATH=$(pwd)/scripts:$PATH

                # needed for lualatex on remote action runner
                export LC_ALL=C
              '';
            }
        );
      };
}
