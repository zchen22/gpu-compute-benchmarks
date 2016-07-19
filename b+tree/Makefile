BENCHMARK = b+tree

CWD = $(shell pwd)
SRCDIR = src
OBJDIR = obj
BINDIR = bin
DATADIR = $(CWD)/../../benchmarks_data/$(BENCHMARK)

CUSRC = $(SRCDIR)/kernel/kernel_gpu_cuda_wrapper.cu \
        $(SRCDIR)/kernel/kernel_gpu_cuda_wrapper_2.cu
CSRC = $(SRCDIR)/main.c \
       $(SRCDIR)/util/cuda/cuda.cu \
       $(SRCDIR)/util/num/num.c \
       $(SRCDIR)/util/timer/timer.c
OBJ = $(patsubst $(SRCDIR)/kernel/%.cu,$(OBJDIR)/%.o,$(CUSRC)) \
      $(OBJDIR)/main.o \
      $(OBJDIR)/cuda.o \
      $(OBJDIR)/num.o \
      $(OBJDIR)/timer.o
BIN = $(BINDIR)/$(BENCHMARK)
DATA1 = $(DATADIR)/mil.txt
DATA2 = $(DATADIR)/command.txt
CMD = ./$(BENCHMARK) file $(DATA1) command $(DATA2) | tee sim.out
CMD1 = PTX_SIM_MODE_FUNC=1 $(CMD)
CMD2 = $(CMD)

INC = -I$(SRCDIR)
NVFLAGS = -arch sm_20 $(INC)

all: makedir $(BIN)

makedir:
	mkdir -p $(OBJDIR)
	mkdir -p $(BINDIR)

$(BIN): $(OBJ)
	nvcc -o $@ $^

$(OBJDIR)/%.o: $(SRCDIR)/kernel/%.cu
	nvcc -o $@ $(NVFLAGS) -c $<

$(OBJDIR)/main.o: $(SRCDIR)/main.c
	nvcc -o $@ $(NVFLAGS) -c $<

$(OBJDIR)/cuda.o: $(SRCDIR)/util/cuda/cuda.cu
	nvcc -o $@ $(NVFLAGS) -c $<

$(OBJDIR)/num.o: $(SRCDIR)/util/num/num.c
	nvcc -o $@ $(NVFLAGS) -c $<

$(OBJDIR)/timer.o: $(SRCDIR)/util/timer/timer.c
	nvcc -o $@ $(NVFLAGS) -c $<

run0-func:
	cp ../vanilla.config $(BINDIR)/gpgpusim.config
	cp ../config_fermi_islip.icnt $(BINDIR)
	cp ../gpuwattch_gtx480.xml $(BINDIR)
	cd $(BINDIR); $(CMD1); mv sim.out sim-func.out

run0-timing:
	cp ../vanilla.config $(BINDIR)/gpgpusim.config
	cp ../config_fermi_islip.icnt $(BINDIR)
	cp ../gpuwattch_gtx480.xml $(BINDIR)
	cd $(BINDIR); $(CMD2); mv sim.out sim-timing.out

run1:
	cp ../base.config $(BINDIR)/gpgpusim.config
	cp ../config_fermi_islip.icnt $(BINDIR)
	cp ../gpuwattch_gtx480.xml $(BINDIR)
	cd $(BINDIR); $(CMD1)

run2:
	cp ../base.config $(BINDIR)/gpgpusim.config
	cp ../config_fermi_islip.icnt $(BINDIR)
	cp ../gpuwattch_gtx480.xml $(BINDIR)
	cd $(BINDIR); $(CMD2); mv sim.out sim-base.out
	cp ../sv.config $(BINDIR)/gpgpusim.config
	cp ../config_fermi_islip.icnt $(BINDIR)
	cp ../gpuwattch_gtx480.xml $(BINDIR)
	cd $(BINDIR); $(CMD2); mv sim.out sim-sv.out

clean:
	rm -fr $(BINDIR) $(OBJDIR)

