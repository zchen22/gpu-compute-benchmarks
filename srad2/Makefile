BENCHMARK = srad_v2

SRCDIR = src
OBJDIR = obj
BINDIR = bin

CUSRC = $(SRCDIR)/srad.cu
OBJ = $(patsubst $(SRCDIR)/%.cu,$(OBJDIR)/%.o,$(CUSRC))
BIN = $(BINDIR)/$(BENCHMARK)
CMD = ./$(BENCHMARK) 2048 2048 0 127 0 127 0.5 2 | tee sim.out
CMD1 = PTX_SIM_MODE_FUNC=1 $(CMD)
CMD2 = $(CMD)

NVFLAGS = -arch sm_20

all: makedir $(BIN)

include ../common.mk

