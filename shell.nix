{ pkgs ? import <nixpkgs> {} }:

(pkgs.buildFHSEnv {
  name = "mcms-content-service";
  targetPkgs = pkgs: (with pkgs;
    [ 
      docker-compose
      python312
      uv
    ]);
  runScript = "bash";
}).env
