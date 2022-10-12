#
# ~/.bash_aliases: included by ~/.bashrc.
#

BIN_TREE=/usr/bin/tree

alias treegit-included='${BIN_TREE} -apugh'
alias treell='${BIN_TREE} -apugh -I ".git"'
alias tree='${BIN_TREE} -a -I ".git"'

