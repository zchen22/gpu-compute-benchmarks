BENCHMARK = srad_v1

SRCDIR = src
OBJDIR = obj
BINDIR = bin

CUSRC = $(SRCDIR)/main.cu
OBJ = $(patsubst $(SRCDIR)/%.cu,$(OBJDIR)/%.o,$(CUSRC))
BIN = $(BINDIR)/$(BENCHMARK)
CMD = ./$(BENCHMARK) 10 0.5 502 458 | tee sim.out
CMD1 = PTX_SIM_MODE_FUNC=1 $(CMD)
CMD2 = $(CMD)

NVFLAGS = -arch sm_20

all: makedir $(BIN)

include ../common.mk

