BENCHMARK = histo

CWD = $(shell pwd)
SRCDIR = src
OBJDIR = obj
BINDIR = bin
DATADIR = $(CWD)/../../benchmarks_data/$(BENCHMARK)

CUSRC = $(wildcard $(SRCDIR)/*.cu)
CSRC = $(wildcard $(SRCDIR)/*.c)
OBJ = $(patsubst $(SRCDIR)/%.cu,$(OBJDIR)/%.o,$(CUSRC)) \
      $(patsubst $(SRCDIR)/%.c,$(OBJDIR)/%.o,$(CSRC))
BIN = $(BINDIR)/$(BENCHMARK)
DATA = $(DATADIR)/img.bin
CMD = ./$(BENCHMARK) -i $(DATA) -o ref.bmp -- 20 4 | tee sim.out
CMD1 = PTX_SIM_MODE_FUNC=1 $(CMD)
CMD2 = $(CMD)

INC = -I$(SRCDIR)
NVFLAGS = -arch sm_20 $(INC)

all: makedir $(BIN)

include ../common.mk

