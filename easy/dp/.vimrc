set nocompatible              " required
filetype off                  " required
" set the runtime path to include Vundle and initialize
set rtp =~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')
" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'
" Add all your plugins here (note older versions of Vundle used Bundle instead of Plugin)
" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

" 設定外觀 -------------------------------------
set number                      "顯示行號 
set showtabline=0               "隱藏頂部標籤欄"
set guioptions-=r               "隱藏右側滾動條" 
set guioptions-=L               "隱藏左側滾動條"
set guioptions-=b               "隱藏底部滾動條"
set cursorline                  "突出顯示當前行"
set cursorcolumn                "突出顯示當前列"
set langmenu=zh_CN.UTF-8        "顯示中文選單
" 變成輔助 -------------------------------------
syntax on                           "開啟語法高亮
set nowrap                      "設定程式碼不折行"
set fileformat=unix             "設定以unix的格式儲存檔案"
set cindent                     "設定C樣式的縮排格式"
set tabstop=4                   "一個 tab 顯示出來是多少個空格，預設 8
set shiftwidth=4                "每一級縮排是多少個空格
set backspace =indent,eol,start "set backspace&可以對其重置
set showmatch                   "顯示匹配的括號"
set scrolloff=5                 "距離頂部和底部5行"
set laststatus=2                "命令列為兩行"
" 其他雜項 -------------------------------------
set mouse=a                     "啟用滑鼠"
set selection=exclusive
set selectmode=mouse,key
set matchtime=5
set ignorecase                  "忽略大小寫"
set incsearch
set hlsearch                    "高亮搜尋項"
set noexpandtab                 "不允許擴充套件table"
set whichwrap =<,>,h,l
set autoread
