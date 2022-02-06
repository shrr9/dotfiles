call plug#begin('~/.local/share/site/autoload/plug.vim')

Plug 'preservim/nerdtree'

call plug#end()

map <C-n> :NERDTreeToggle<CR>

set laststatus=2
set statusline+=%F
set expandtab
set smartindent
set ts=4 sw=4
set number
set clipboard=unnamedplus
set cuc
set relativenumber
set cul
set incsearch
set scrolloff=8
