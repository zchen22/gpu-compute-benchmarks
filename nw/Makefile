BENCHMARK = nw

SRCDIR = src
OBJDIR = obj
BINDIR = bin

SRC = $(SRCDIR)/needle.cu
OBJ = $(patsubst $(SRCDIR)/%.cu,$(OBJDIR)/%.o,$(SRC))
BIN = $(BINDIR)/$(BENCHMARK)
CMD = ./$(BENCHMARK) 2048 10 | tee sim.out
CMD1 = PTX_SIM_MODE_FUNC=1 $(CMD)
CMD2 = $(CMD)

NVFLAGS = -arch sm_20

all: makedir $(BIN)

include ../common.mk

