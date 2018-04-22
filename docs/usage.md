# Usage

You can list all NEO command with `help`

``` bash
$ neo --help
```

## Authentication

Use `neo login` to log in. `neo logout` to do the opposite.

## Creation

``` bash
$ neo create
```

NEO creates `neo.yml` for you if it doesn't find one. Then it will
guide you trough questions to do the right job for you.

It will ask you the 'stack' and 'template' you want to create. Then
fill 'key-pairs' and 'network' configuration. The last step is to
setup your 'vm' where you are asked to choose 'image name' and
'flavor'.

When you sure with the configuration. Hit 'y/yes' to continue to
deploy.

## List your stuffs

``` bash
$ neo ls --help
```

- `stack`

List all the stacks

- `vm`

List all virtual machines

- `network`

List all network

e.g `neo ls stack`

## Remove your stuffs

``` bash
$ neo rm
```

It will delete your stack, network and machine

## Update

``` bash
$ neo update
```
Use `update` to see your changes.

## Attach

Attach local standard input, output, and error streams to a running
stack or virtual machine


``` bash
$ neo attach vm
```

`neo attach` will read neo.yml configuration automatically if you
didn't pass the <id> of your vm.

You can also specify your running vm id manually with

``` bash
$ neo attach vm <your-vm-id>
```
