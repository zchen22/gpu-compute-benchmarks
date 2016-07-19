BENCHMARK = vectorAdd

SRCDIR = src
OBJDIR = obj
BINDIR = bin

SRC = $(SRCDIR)/vectorAdd.cu
OBJ = $(patsubst $(SRCDIR)/%.cu,$(OBJDIR)/%.o,$(SRC))
BIN = $(BINDIR)/$(BENCHMARK)
CMD = ./$(BENCHMARK) | tee sim.out
CMD1 = PTX_SIM_MODE_FUNC=1 $(CMD)
CMD2 = $(CMD)

NVFLAGS = -arch sm_20

all: makedir $(BIN)

include ../common.mk

