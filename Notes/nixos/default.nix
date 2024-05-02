# default.nix
with (import <nixpkgs> {});
mkShell {
  buildInputs = [
    tldr
    ripgrep
    gcc
  ];
}