BENCHMARK = stencil

CWD = $(shell pwd)
SRCDIR = src
OBJDIR = obj
BINDIR = bin
DATADIR = $(CWD)/../../benchmarks_data/$(BENCHMARK)

CUSRC = $(SRCDIR)/main.cu
CCSRC = $(wildcard $(SRCDIR)/*.cc)
CSRC = $(wildcard $(SRCDIR)/*.c)
OBJ = $(patsubst $(SRCDIR)/%.cu,$(OBJDIR)/%.o,$(CUSRC)) \
      $(patsubst $(SRCDIR)/%.cc,$(OBJDIR)/%.o,$(CCSRC)) \
      $(patsubst $(SRCDIR)/%.c,$(OBJDIR)/%.o,$(CSRC))
BIN = $(BINDIR)/$(BENCHMARK)
DATA = $(DATADIR)/128x128x32.bin
CMD = ./$(BENCHMARK) -i $(DATA) -o 128x128x32.out -- 128 128 32 100 | \
      tee sim.out
CMD1 = PTX_SIM_MODE_FUNC=1 $(CMD)
CMD2 = $(CMD)

INC = -I$(SRCDIR)
NVFLAGS = -arch sm_20 $(INC)

all: makedir $(BIN)

include ../common.mk

