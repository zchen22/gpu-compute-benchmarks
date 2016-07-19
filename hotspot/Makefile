BENCHMARK = hotspot

CWD = $(shell pwd)
SRCDIR = src
OBJDIR = obj
BINDIR = bin
DATADIR = $(CWD)/../../benchmarks_data/$(BENCHMARK)

SRC = $(wildcard $(SRCDIR)/*.cu)
OBJ = $(patsubst $(SRCDIR)/%.cu,$(OBJDIR)/%.o,$(SRC))
BIN = $(BINDIR)/$(BENCHMARK)
DATA = $(DATADIR)/temp_512 $(DATADIR)/power_512
CMD = ./$(BENCHMARK) 512 2 2 $(DATA) output.out | tee sim.out
CMD1 = PTX_SIM_MODE_FUNC=1 $(CMD)
CMD2 = $(CMD)

NVFLAGS = -arch sm_20

all: makedir $(BIN)

include ../common.mk

