set t_Co=256

call plug#begin('~/.vim/plugged')

" plugin section

Plug 'pangloss/vim-javascript', { 'for': 'javascript' }

" Extract to VimForScratch web site
Plug 'jiangmiao/auto-pairs'
Plug 'preservim/nerdtree'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'othree/yajs.vim'
Plug 'mxw/vim-jsx'
Plug 'dense-analysis/ale'
Plug'tpope/vim-commentary'
if has('nvim')
  Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
else
  Plug 'Shougo/deoplete.nvim'
  Plug 'roxma/nvim-yarp'
  Plug 'roxma/vim-hug-neovim-rpc'
endif


Plug 'leafgarland/typescript-vim'
Plug 'maxmellon/vim-jsx-pretty'
Plug 'mattn/emmet-vim'

Plug 'prettier/vim-prettier', { 'do': 'yarn install', 'for': ['javascript', 'typescript', 'css', 'less', 'scss', 'json', 'graphql', 'markdown', 'vue', 'yaml', 'html'] }
Plug 'SirVer/ultisnips'
Plug 'mlaursen/vim-react-snippets'
Plug 'terryma/vim-multiple-cursors'

" Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'ryanoasis/vim-devicons'
Plug 'ctrlpvim/ctrlp.vim' " fuzzy find files
" Plug 'scrooloose/nerdcommenter'

Plug 'HerringtonDarkholme/yats.vim' " TS Syntax

" ============================
" Nuevos Agregados por mi
" ============================

Plug 'sheerun/vim-polyglot'
" Resaltado de sintaxis para cada lenguaje
" Plug 'hail2u/vim-css3-syntax', { 'for': 'css' }
" Plug 'othree/html5.vim', { 'for': 'html' }
" Plug 'plasticboy/vim-markdown', { 'for': 'markdown' }
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'  " Temas para airline
Plug 'Shougo/echodoc.vim'
Plug 'sirver/ultisnips'
Plug 'honza/vim-snippets'
Plug 'tpope/vim-fugitive'

Plug 'bluz71/vim-nightfly-guicolors'
Plug 'carlitux/deoplete-ternjs', { 'do': 'npm install -g tern' }
Plug 'ternjs/tern_for_vim'

Plug 'python-mode/python-mode', { 'for': 'python', 'branch': 'develop' }

Plug 'autozimu/LanguageClient-neovim', { 'branch': 'next', 'do': 'bash install.sh' }

Plug 'deoplete-plugins/deoplete-jedi'
" ============================
" Fin Nuevos Agregados por mi
" ============================
" end vim-plug
call plug#end()

" ======================================================================
" CONFIGURACIONES
" ======================================================================

set bs=indent,eol,start " backspace over everything in insert mode

let g:_uspy = ':py3'

execute pathogen#infect()
syntax on
filetype plugin indent on

if (has("termguicolors"))
  set termguicolors
endif


colorscheme nightfly

let g:deoplete#enable_at_startup=1
let g:prettier#autoformat = 0
autocmd BufWritePre *.js,*.jsx,*.mjs,*.ts,*.tsx,*.css,*.less,*.scss,*.json,*.graphql,*.md,*.vue,*.yaml,*.html PrettierAsync
let g:airline_theme='light'

let g:deoplete#sources#jedi#enable_typeinfo = 1

" FORMATTERS
au FileType javascript setlocal formatprg=prettier
au FileType javascript.jsx setlocal formatprg=prettier
au FileType typescript setlocal formatprg=prettier\ --parser\ typescript
au FileType html setlocal formatprg=js-beautify\ --type\ html
au FileType scss setlocal formatprg=prettier\ --parser\ css
au FileType css setlocal formatprg=prettier\ --parser\ css

" MI CONFIGURACION INICIO
" ===========================
" AIRLINE
" enable tabline
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#left_sep = ''
let g:airline#extensions#tabline#left_alt_sep = ''
let g:airline#extensions#tabline#right_sep = ''
let g:airline#extensions#tabline#right_alt_sep = ''

let g:airline#extensions#tabline#fnamemod = ':t'  " Mostrar sólo el nombre del archivo
"let g:airline#extensions#tabline#left_sep = ' '
"let g:airline#extensions#tabline#left_alt_sep = '|'
"let g:airline#extensions#tabline#formatter = 'default'

" enable powerline fonts
let g:airline_powerline_fonts = 1

" Switch to your current theme
let g:airline_theme = 'powerlineish'

" Always show tabs
set showtabline=2

" We don't need to see things like -- INSERT -- anymore
set noshowmode

" IDENT
" No mostrar en ciertos tipos de buffers y archivos
let g:indentLine_fileTypeExclude = ['text', 'sh', 'help', 'terminal']
let g:indentLine_bufNameExclude = ['NERD_tree.*', 'term:.*']

" ECHODOC
let g:echodoc#enable_at_startup = 1
let g:echodoc#type = "echo  "
set noshowmode  " No mostrar el modo actual (echodoc hace uso de este espacio)

" ULTISPINET ==================
" Expandir snippet con Ctrl + j
let g:UltiSnipsExpandTrigger = '<c-j>'
" Ir a siguiente ubicacion con Ctrl + j
let g:UltiSnipsJumpForwardTrigger = '<c-j>'
" Ir a anterior ubicacion con Ctrl + k
let g:UltiSnipsJumpBackwardTrigger = '<c-k>'
" If you want :UltiSnipsEdit to split your window.
let g:UltiSnipsEditSplit="vertical"

" ALE
" Mostrar mejor mensajes de error
let g:ale_echo_msg_error_str = 'E'
let g:ale_echo_msg_warning_str = 'W'
let g:ale_echo_msg_format = '[%linter%] %s [%severity%]'
let g:ale_linters = {
\   'python': ['flake8', 'pylint'],
\   'javascript': ['eslint'],
\   'vue': ['eslint']
\}
let g:ale_fixers = {
  \    'javascript': ['eslint'],
  \    'typescript': ['prettier', 'tslint'],
  \    'vue': ['eslint'],
  \    'scss': ['prettier'],
  \    'html': ['prettier'],
  \    'reason': ['refmt']
\}
let g:ale_fix_on_save = 1
let g:ale_completion_tsserver_autoimport = 1
let g:ale_completion_enabled = 1
"call deoplete#custom#option('sources', {'_': ['ale', 'foobar'],})
" extraido de https://www.rockyourcode.com/developing-with-elixir-in-vim/#elixir-language-server
let g:ale_sign_error = '✘'
let g:ale_sign_warning = '⚠'
let g:ale_lint_on_enter = 0
let g:ale_lint_on_text_changed = 'never'
highlight ALEErrorSign ctermbg=NONE ctermfg=red
highlight ALEWarningSign ctermbg=NONE ctermfg=yellow
let g:ale_linters_explicit = 1
let g:ale_lint_on_save = 1

" DEVICONS
set encoding=UTF-8 

"LANGUAGESERVER
let g:LanguageClient_serverCommands = {
    \ 'javascript': ['javascript-typescript-stdio'],
    \ 'python': ['/usr/local/bin/pyls'],
    \ 'javascript.jsx': ['tcp://127.0.0.1:2089'],
    \ }
nnoremap <leader>l :call LanguageClient_contextMenu()<CR>
nnoremap K :call LanguageClient#textDocument_hover()<CR>
nnoremap gd :call LanguageClient#textDocument_definition()<CR>
nnoremap <leader>r :call LanguageClient#textDocument_rename()<CR>

" AUTOPAIR
let g:AutoPairsFlyMode = 0
let g:AutoPairsShortcutBackInsert = '<M-b>'

" ===========================
" MI CONFIGURACION FIN
